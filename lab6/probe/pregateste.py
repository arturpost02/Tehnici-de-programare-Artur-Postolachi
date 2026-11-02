import os,base64,hashlib,random,io,zipfile
from PIL import Image
HERE=os.path.dirname(os.path.abspath(__file__))
def scrie(nume,date):
    with open(os.path.join(HERE,nume),'wb') as f:
        f.write(date if isinstance(date,bytes) else date.encode())
    print('scris:',nume)
clar=b'FLAG{straturi_de_encoding}'
scrie('mesaj.txt',base64.b64encode(base64.b64encode(clar.hex().encode())))
secret=b"Un singur octet tine tot secretul... gaseste-l! FLAG{xor_un_octet}"
scrie('xor.bin',bytes(b^128 for b in secret))
parole=['password','dragon','qwerty','letmein','monkey']
cuvinte=['123456','football','iloveyou']+parole+['admin','welcome']
random.seed(6);random.shuffle(cuvinte)
scrie('hashuri.txt','\n'.join(hashlib.md5(p.encode()).hexdigest() for p in parole)+'\n')
scrie('wordlist.txt','\n'.join(cuvinte)+'\n')
img=Image.new('RGB',(640,480),(70,110,160))
exif=Image.Exif()
exif[0x010F]='Apple'
exif[0x0110]='iPhone 13'
exif[0x0132]='2026:09:14 10:30:00'
exif[0x8825]={1:'N',2:(47.0,1.0,0.0),3:'E',4:(28.0,51.0,27.0)}
img.save(os.path.join(HERE,'foto.jpg'),exif=exif,quality=90)
print('scris: foto.jpg')
p=os.path.join(HERE,'ascuns.png')
Image.new('RGB',(320,240),(40,160,90)).save(p)
buf=io.BytesIO()
with zipfile.ZipFile(buf,'w') as z:z.writestr('secret.txt','FLAG{ascuns_prin_carving}\n')
with open(p,'ab') as f:f.write(buf.getvalue())
print('scris: ascuns.png')
inner=bytes(b^128 for b in b'FLAG{lant_complet_despicat}')
scrie('challenge.bin',base64.b64encode(inner))
scrie('challenge_hint.txt','Un strat de base64 peste un XOR cu cheie de un octet. Verificare: md5 al textului clar = '+hashlib.md5(b'FLAG{lant_complet_despicat}').hexdigest()+'\n')
print('Gata:',HERE)
