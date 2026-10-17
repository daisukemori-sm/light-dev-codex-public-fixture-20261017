import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse
from policy import can_cancel
from summary import status_label
HTML = """<!doctype html><html lang="ja"><meta charset="utf-8"><title>申請取り消し試験</title><body><h1>申請取り消し</h1><label>状態<select id="status"><option value="pending">申請中</option><option value="approved">承認済み</option></select></label><label>申請者<input id="owner" value="alice"></label><label>操作する人<input id="actor" value="alice"></label><button id="cancel">取り消し可否を確認</button><output id="result"></output><script>document.querySelector('#cancel').onclick=async()=>{const q=new URLSearchParams();for(const k of ['status','owner','actor'])q.set(k,document.getElementById(k).value);const r=await fetch('/api/cancel?'+q);document.getElementById('result').textContent=(await r.json()).allowed?'取り消し可能':'取り消し不可';};</script></body></html>"""
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url=urlparse(self.path)
        if url.path=='/api/cancel':
            q=parse_qs(url.query)
            value=lambda k: q.get(k,[''])[0]
            body=json.dumps({'allowed':can_cancel(value('status'),value('owner'),value('actor'))}).encode()
            mime='application/json'
        elif url.path=='/api/label':
            body=json.dumps({'label':status_label(parse_qs(url.query).get('status',[''])[0])},ensure_ascii=False).encode();mime='application/json'
        else: body=HTML.encode();mime='text/html; charset=utf-8'
        self.send_response(200);self.send_header('Content-Type',mime);self.end_headers();self.wfile.write(body)
    def log_message(self,*args): pass
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=8765);a=p.parse_args()
    server=ThreadingHTTPServer(('127.0.0.1',a.port),Handler)
    print('READY http://127.0.0.1:'+str(server.server_port),flush=True);server.serve_forever()
