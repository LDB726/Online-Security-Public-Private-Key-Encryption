# These two functions will help determine if two numbers are coprimes #
# Returns the greatest common denominator for two numbers
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p
# Determines if two numbers are coprime. Returns True or False
def is_coprime(x, y):
    return gcd(x, y) == 1

# Returns a list of all the prime numbers from 2 to n
def primes_less_than(n):
	all_primes=[]
	prime = [True for i in range(n + 1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p ** 2, n + 1, p):
				prime[i] = False
		p += 1
	prime[0]= False
	prime[1]= False
	# Print all prime numbers
	for p in range(n + 1):
		if prime[p]:
			all_primes.append(p)
	return all_primes
def encrypt(n,e, letter):
	x=ord(letter)
	y=(x**e)%n
	newletter=chr(y)
	return newletter
def decrypt(n,d, enc):
	x=ord(enc)
	y=(x**d)%n
	newletter=chr(y)
	return newletter
def encrypt_message(n,e,message):
	mes=list(message)
	newm=[]
	for let in mes:
		y=((ord(let))**e)%n
		z=chr(y)
		newm.append(z)
	return newm
def decrypt_message(n,d, list):
	oldm=[]
	for let in list:
		y=((ord(let))**d)%n
		z=chr(y)
		oldm.append(z)
		realm = "".join(oldm)
	return realm


print("All primes less than 1,000:\n"+str(primes_less_than(1000)))
p=67
q=97
e=23
d=551
print(gcd(p, q))
t=((p-1)*(q-1))
n=p*q
for x in range(10):
	m=x*23
	z=m%t
	if z==1:
		print(m)
		print(str(z)+"!!!!")
print(12673/23)
newl = encrypt(n,e, "p")
oldl = decrypt(n, d, newl)
newm = encrypt_message(n,e,"hello world")
oldm = decrypt_message(n,d,newm)
print(1234567)
print(newl)
print(oldl)
print(newm)
print(oldm)