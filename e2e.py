import json
import threading
import urllib.request
from urllib.parse import urlencode
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
    allowed_pairs = {('alice', 'alice'), ('bob', 'bob')}
    scenarios = 0
    for status in ('pending', 'approved', 'unknown', ''):
        for owner in ('alice', 'bob', ''):
            for actor in ('alice', 'bob', ''):
                expected = (owner, actor) in allowed_pairs if status == 'pending' else False
                query = urlencode({'status': status, 'owner': owner, 'actor': actor})
                actual = get(query)
                assert actual is expected, (status, owner, actor, expected, actual)
                scenarios += 1
    print(f'PASS: local API e2e 4 existing + {scenarios} matrix scenarios')
finally: s.shutdown();s.server_close();t.join()
