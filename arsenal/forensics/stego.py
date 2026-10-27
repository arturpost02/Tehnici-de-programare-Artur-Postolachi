"""Lucrarea B5-B6: scrie si citeste un mesaj LSB."""
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[2]
def ascunde(sursa,destinatie,mesaj):
    with Image.open(sursa) as original:img=original.convert('RGB')
    biti=''.join(f'{b:08b}' for b in mesaj.encode()+b'\x00')
    canale=[c for p in img.getdata() for c in p]
    if len(biti)>len(canale):raise ValueError('Mesaj prea lung')
    for i,bit in enumerate(biti):canale[i]=(canale[i]&~1)|int(bit)
    img.putdata([tuple(canale[i:i+3]) for i in range(0,len(canale),3)])
    img.save(destinatie,format='PNG')
def dezvaluie(cale):
    rezultat=bytearray()
    biti=''
    with Image.open(cale) as img:
        for p in img.convert('RGB').getdata():
            for c in p:
                biti+=str(c&1)
                if len(biti)==8:
                    x=int(biti,2)
                    if x==0:return rezultat.decode()
                    rezultat.append(x)
                    biti=''
    raise ValueError('Terminatorul lipseste')
def main():
    destinatie=ROOT/'stego.png'
    ascunde(ROOT/'probe'/'foto.jpg',destinatie,'FLAG{ascuns_in_pixeli}')
    print('Fisier creat:',destinatie)
    print('Mesaj LSB:',dezvaluie(destinatie))
if __name__=='__main__':main()
