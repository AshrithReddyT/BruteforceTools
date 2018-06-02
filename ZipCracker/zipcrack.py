from itertools import chain, product
import zipfile

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))
def cracker(zfile,attempt,filename):
    try:
        zfile.extractall(filename,pwd=attempt.strip())
        return attempt
    except:
        return None

file = raw_input("Enter The Zip File name: ")
filename = raw_input("Enter The File name after extraction: ")
method = raw_input("Enter the method of cracking: 1.Bruteforce 2.Dictionary: ")
zfile = zipfile.ZipFile(file,'r')
if int(method) == 1:
    charset='EeTtAaOoIiNnSsHhRrDdLlCcUuMmWwFfGgYyPpBbVvKkJjXxQqZz1234567890'
    for attempt in bruteforce(charset, 10):
        if cracker(zfile,attempt,filename):
            print 'The Password is:'
            print attempt
            break
elif int(method) == 2:
    with open("dictionary.txt","r") as f:
        words = f.read().split("\n")
        for attempt in words:
            if cracker(zfile,attempt,filename):
                print 'The Password is:'
                print attempt.strip()
                break
else:
    print "Choose a valid option"
