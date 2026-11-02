from pathlib import Path
from arsenal.forensics.decode import desfa,decodare_straturi,sparge_xor,sparge_hash
from arsenal.forensics.forensics import tip_real,metadata,carving
from arsenal.forensics.stego import ascunde,dezvaluie
ROOT=Path(__file__).resolve().parents[1]
def test_base64():
    t,b=desfa('U2FsdXQ=')
    assert t=='base64' and b==b'Salut'
def test_straturi():
    p,b=decodare_straturi((ROOT/'probe'/'mesaj.txt').read_text().strip())
    assert p==['base64','base64','hex'] and b==b'FLAG{straturi_de_encoding}'
def test_xor():
    assert sparge_xor((ROOT/'probe'/'xor.bin').read_bytes())[0]==128
def test_hash():
    h=(ROOT/'probe'/'hashuri.txt').read_text().splitlines()[0]
    cuv=(ROOT/'probe'/'wordlist.txt').read_text().splitlines()
    assert sparge_hash(h,cuv)==('md5','password')
def test_magic_gps():
    assert tip_real(ROOT/'probe'/'foto.jpg')=='jpeg'
    gps=metadata(ROOT/'probe'/'foto.jpg')
    assert abs(gps['latitudine']-47.0167)<0.001
    assert abs(gps['longitudine']-28.8575)<0.001
def test_carving(tmp_path):
    poz,continut=carving(ROOT/'probe'/'ascuns.png',tmp_path/'gasit.zip')
    assert poz>0 and continut==[('secret.txt','FLAG{ascuns_prin_carving}\n')]
def test_stego(tmp_path):
    cale=tmp_path/'stego.png'
    ascunde(ROOT/'probe'/'foto.jpg',cale,'FLAG{ascuns_in_pixeli}')
    assert dezvaluie(cale)=='FLAG{ascuns_in_pixeli}'
