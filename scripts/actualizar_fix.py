"""Descarga únicamente el dato público FIX; nunca escribe ni imprime el token."""
import os,json,urllib.request
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal
out=Path('fx.json')
token=os.environ.get('BANXICO_TOKEN','')
if not token:
    print('BANXICO_TOKEN no configurado: se conserva la copia FIX con su fecha original.')
    raise SystemExit(0)
url='https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno'
try:
    req=urllib.request.Request(url,headers={'Bmx-Token':token,'Accept':'application/json'})
    with urllib.request.urlopen(req,timeout=20) as response:data=json.load(response)
    points=[]
    for series in data['bmx']['series']:
        if series.get('idSerie')!='SF43718':continue
        for point in series.get('datos',[]):
            try:
                rate=Decimal(point['dato'].replace(',',''))
                date=datetime.strptime(point['fecha'],'%d/%m/%Y').date()
                if rate.is_finite() and rate>0 and date<=datetime.now(timezone.utc).date():points.append((date,rate))
            except (ValueError,ArithmeticError):continue
    if not points:raise ValueError('Sin puntos válidos')
    date,rate=max(points,key=lambda x:x[0])
    snapshot=dict(rate=str(rate),date=date.isoformat(),series='SF43718',unit='MXN por USD',source=url,retrieved_at=datetime.now(timezone.utc).isoformat(),status='disponible',error=None)
    out.write_text(json.dumps(snapshot,indent=2),encoding='utf-8')
    print('FIX actualizado:',date,str(rate),'MXN por USD')
except Exception:
    print('No fue posible consultar Banxico. La publicación conserva la copia anterior y su fecha original.')
    if not out.exists():raise SystemExit(1)
