"""Verify the public site's local resources and evidence payload before release."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'docs' if (ROOT/'docs/index.html').exists() else ROOT
class Document(HTMLParser):
    def __init__(self):super().__init__();self.refs=[];self.lang=False;self.h1=0;self.viewport=False;self.csp=False;self.in_data=False;self.data='';self.ids=set();self.duplicate_ids=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):
            if a['id'] in self.ids:self.duplicate_ids.append(a['id'])
            self.ids.add(a['id'])
        if tag=='html':self.lang=bool(a.get('lang'))
        if tag=='h1':self.h1+=1
        if tag=='meta':
            self.viewport |= a.get('name')=='viewport'
            self.csp |= a.get('http-equiv','').lower()=='content-security-policy'
        if tag=='script' and a.get('type')=='application/json':self.in_data=True
        for k in ['src','href']:
            if a.get(k):self.refs.append(a[k])
    def handle_endtag(self,tag):
        if tag=='script':self.in_data=False
    def handle_data(self,data):
        if self.in_data:self.data+=data
documents={}
for path in SITE.rglob('*.html'):
    if '.git' in path.parts:continue
    p=Document();p.feed(path.read_text());assert p.lang and p.h1==1 and p.viewport and p.csp,path
    assert not p.duplicate_ids,(path,p.duplicate_ids)
    documents[path.resolve()]=p
    if p.data:json.loads(p.data)
for path,p in documents.items():
    for ref in p.refs:
        url=urlsplit(ref)
        if url.scheme or url.netloc:continue
        target=(SITE/unquote(url.path).lstrip('/') if url.path.startswith('/') else path.parent/unquote(url.path)).resolve() if url.path else path
        assert target.is_relative_to(SITE.resolve()),(path,ref,'outside site')
        if target.is_dir():target=target/'index.html'
        assert target.exists(),(path,ref)
        if url.fragment and target in documents:
            assert unquote(url.fragment) in documents[target].ids,(path,ref,'missing anchor')
print(f'{len(documents)} pages: local resources, fragment targets, semantics and evidence payload passed.')
