"""Lucrarea B1-B4: analiza fisierelor proprii."""
import re,zipfile
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
ROOT=Path(__file__).resolve().parents[2]
PROBE=ROOT/'probe'
def tip_real(cale):
    with open(cale,'rb') as f:cap=f.read(8)
    for sig,nume in [(b'%PDF','pdf'),(b'\x89PNG','png'),(b'\xff\xd8','jpeg'),(b'PK\x03\x04','zip/docx')]:
        if cap.startswith(sig):return nume
    return 'necunoscut: '+cap.hex()
def siruri_citibile(cale,minim=4):
    return [m.decode('ascii') for m in re.findall(rb'[ -~]{4,}',Path(cale).read_bytes())]
def dms_zecimal(dms,ref):
    g,m,s=(float(x) for x in dms)
    v=g+m/60+s/3600
    return -v if ref in ('S','W') else v
def metadata(cale):
    with Image.open(cale) as im:
        exif=im.getexif()
        rezultat={TAGS.get(k,str(k)):str(v) for k,v in exif.items() if k!=34853}
        gps=exif.get_ifd(34853) if 34853 in exif else {}
        if all(k in gps for k in (1,2,3,4)):
            rezultat['latitudine']=dms_zecimal(gps[2],gps[1])
            rezultat['longitudine']=dms_zecimal(gps[4],gps[3])
        return rezultat
def carving(cale,iesire):
    date=Path(cale).read_bytes()
    poz=date.find(b'PK\x03\x04')
    if poz<0:return None,[]
    Path(iesire).write_bytes(date[poz:])
    with zipfile.ZipFile(iesire) as z:
        continut=[(n,z.read(n).decode('utf-8',errors='replace')) for n in z.namelist()]
    return poz,continut
def main():
    for n in ('foto.jpg','ascuns.png'):print(n,tip_real(PROBE/n))
    print('strings:',siruri_citibile(PROBE/'ascuns.png')[-8:])
    print('EXIF/GPS:',metadata(PROBE/'foto.jpg'))
    poz,continut=carving(PROBE/'ascuns.png',PROBE/'gasit.zip')
    print('ZIP offset:',poz,'continut:',continut)
if __name__=='__main__':main()
