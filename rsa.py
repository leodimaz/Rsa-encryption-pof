from fractions import gcd
from random import randint

def lcm(a, b):
    if a > b:
        greater=a
    else:
        greater=b
    while True:
        if greater%a == 0 and greater%b == 0:
            lcm = greater
            break
        greater += 1
    return lcm

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def valid_prime(a):
    if a<3:
        return False
    for x in xrange(2,a):
        if a%x==0:
            #print "{}%{}={}".format(a,x,a%x)
            return False
        else:
            #print "{}%{}={}".format(a,x,a%x)
            if x==a-1:
                return True

def valid_primes(a):
    primes = []
    for x in xrange(3,a):
        if valid_prime(x):
            primes.append(x)
    return primes

def valid_coprime(a,b):
    if gcd(a,b)==1:
        return True
    else:
        return False

def valid_coprimes(a,b):
    coprimes = []
    for x in range(len(a)):
        if valid_coprime(b,a[x]):
            coprimes.append(a[x])
    return coprimes

def get_pq(status=0):
    global p,q
    if status==0:
        try:
            p = int(raw_input("=> Enter first prime number: "))
        except:
            print "[-] p must be valid int"
            return get_pq(0)
        if valid_prime(p)==False:
            print "[-] p must be prime"
            return get_pq(0)
    status=1
    if status==1:
        try:
            q = int(raw_input("=> Enter second prime number: "))
        except:
            print "[-] q must be valid int"
            return get_pq(1)
        if valid_prime(q)==False:
            print "[-] q must be prime"
            return get_pq(1)
    return p,q

def get_msg():
    try:
        message=raw_input("Enter message do you want to encrypt: ")
    except:
        print "[-] Insert valid message"
        return get_msg()
    if message=="":
        print "[-] Message can't be empty"
        return get_msg()

    return message

p,q = get_pq()
n=p*q
phin = lcm(p-1,q-1)
print "[+] p: {}  q: {} => n: {} => PHIn: {}".format(p,q,n,phin)
primes = valid_primes(phin)
coprimes = valid_coprimes(primes,phin)
e = coprimes[randint(0,len(coprimes)-1)]
d=modinv(e,phin)
print "[+] PUBLIC KEY : {}".format(e)
print "[+] PRIVATE KEY: {}".format(d)

message = get_msg()

enc=[(ord(char) ** d) % n for char in message]
dec=''.join([chr((char ** e) % n) for char in enc])

print "MSG: {}\nENC: {}\nDEC: {}".format(message,enc,dec)
