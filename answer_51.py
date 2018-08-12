import math
import itertools
from eratos import eratos
from solve_51 import solve_51
import time

N = 1000000

# You can either calculate the primes with the
# Sieve of Eratosthenes or download a file from the internet

# t0 = time.time()
# primes_N = eratos(N)
# t1 = time.time()

# Primes up to 10^6:
with open('primes_106.txt','r') as file_primes_106:
    primes_106 = file_primes_106.read()

primes_106 = primes_106.replace(',',' ')
primes_106 = primes_106.split(' ')
primes_106 = [i.replace('\n','') for i in primes_106]
primes_106 = [int(i) for i in primes_106]

# Solving Problem 51:
t2 = time.time()
solve_51(N,primes_106,6)
t3 = time.time()
print(f'Time solve_51: {t3-t2}s')
