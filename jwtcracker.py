from itertools import chain, product
import hmac
import hashlib
import base64
import json
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))
def cracker(token,attempt):
    data=token.split(".")
    encoded_sig = data[0]
    payload = data[1]
    final = data[2]
    reqsig = base64_url_decode(final)
    required = encoded_sig+'.'+payload
    sig = base64_url_decode(encoded_sig)
    dat = json.loads(base64_url_decode(payload))
    expected_sig = hmac.new(attempt, msg=required, digestmod=hashlib.sha256).digest()
    if reqsig != expected_sig:
        return None
    else:
        return attempt
def base64_url_decode(inp):
    padding_factor = (4 - len(inp) % 4) % 4
    inp += "="*padding_factor 
    return base64.b64decode(unicode(inp).translate(dict(zip(map(ord, u'-_'), u'+/'))))

token = raw_input("Enter The Token: ")
charset='abcdefghijklmnopqrstuvwxyz1234567890'
for attempt in bruteforce(charset, 10):
    if cracker(token,attempt):
        print 'The Secret is:'
        print attempt
        break


