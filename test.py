with open('primes_106.txt','r') as file_primes_106:
    data = file_primes_106.read()

data2 = data.replace(',',' ')
data2 = data2.split(' ')
data2 = [i.replace('\n','') for i in data2]
data2 = [int(i) for i in data2]
