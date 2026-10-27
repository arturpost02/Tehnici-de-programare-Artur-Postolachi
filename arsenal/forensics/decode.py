"""Lucrarea A: decoder pentru probele proprii."""
import re,base64,binascii,hashlib,json,argparse
from pathlib import Path
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[2]
def citibil(b):
    return all(32<=x<127 for x in b)
def ghici_strat(s):
    s=s.strip()
    if re.search(r'%[0-9a-fA-F]{2}',s):return 'url'
    if s and len(s)%2==0 and re.fullmatch(r'[0-9a-fA-F]+',s):return 'hex'
    if s and len(s)%4==0 and re.fullmatch(r'[A-Za-z0-9+/]*={0,2}',s):return 'base64'
    return 'necunoscut'
def desfa(s):
    t=ghici_strat(s)
    if t=='url':return t,unquote(s).encode()
    if t=='hex':return t,bytes.fromhex(s)
    if t=='base64':
        try:return t,base64.b64decode(s,validate=True)
        except (binascii.Error,ValueError):pass
    return 'necunoscut',s.encode()
def decodare_straturi(s,maxim=8):
    pasi=[]
    for _ in range(maxim):
        t,b=desfa(s)
        if t=='necunoscut':break
        pasi.append(t)
        try:urmator=b.decode('utf-8')
        except UnicodeDecodeError:return pasi,b
        if urmator==s:break
        s=urmator
        if ghici_strat(s)=='necunoscut':break
    return pasi,s.encode()
def sparge_xor(date):
    for k in range(256):
        text=bytes(b^k for b in date)
        if citibil(text):return k,text.decode()
    return None,None
def sparge_hash(tinta,cuvinte):
    alg={32:'md5',40:'sha1',64:'sha256'}.get(len(tinta))
    if alg:
        for c in cuvinte:
            c=c.strip()
            if hashlib.new(alg,c.encode()).hexdigest()==tinta.lower():return alg,c
    return alg,None
def analiza(intrare,fisier=False):
    if fisier:
        cale=Path(intrare)
        date=cale.read_bytes()
        if cale.name=='xor.bin':
            k,clar=sparge_xor(date)
            return {'strat':'xor','cheie':k,'rezultat':clar}
        intrare=date.decode('utf-8')
    pasi,rez=decodare_straturi(intrare.strip())
    return {'strat':pasi[0] if pasi else 'necunoscut','pasi':pasi,'rezultat':rez.decode('utf-8',errors='replace')}
def main():
    p=argparse.ArgumentParser()
    p.add_argument('intrare')
    p.add_argument('--fisier',action='store_true')
    a=p.parse_args()
    fisa=analiza(a.intrare,a.fisier)
    cale=ROOT/'arsenal'/'forensics'/'fisa.json'
    cale.write_text(json.dumps(fisa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(fisa,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
