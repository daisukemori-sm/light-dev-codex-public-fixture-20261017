import json
import threading
import urllib.request
from http.server import ThreadingHTTPServer
from server import Handler
s=ThreadingHTTPServer(('127.0.0.1',0),Handler)
t=threading.Thread(target=s.serve_forever,daemon=True);t.start()
try:
    def get(query):
        with urllib.request.urlopen('http://127.0.0.1:'+str(s.server_port)+'/api/cancel?'+query) as r: return json.load(r)['allowed']
    assert get('status=pending&owner=alice&actor=alice') is True
    assert get('status=approved&owner=alice&actor=alice') is False
    assert get('status=pending&owner=alice&actor=bob') is False
    assert get('status=pending&owner=&actor=') is False
    print('PASS: local API e2e 4 scenarios')
finally: s.shutdown();s.server_close();t.join()
