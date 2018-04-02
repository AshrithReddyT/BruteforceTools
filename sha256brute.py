from itertools import chain, product
import hashlib
import base64
import json
import hashlib

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))
def cracker(token,attempt):
    hash_object = hashlib.sha256(attempt)
    hex_dig = hash_object.hexdigest()
    if hex_dig != token:
        return None
    else:
        return attempt

token = raw_input("Enter The SHA256 string: ")
charset='abcdefghijklmnopqrstuvwxyz1234567890'
for attempt in bruteforce(charset, 10):
    if cracker(token,attempt):
        print 'The Password is:'
        print attempt
        break
