## Famous Algorithms:

#### Sieve of Eratosthenes

1. An efficient way of getting all the primes under an arbitrary number N.
2. A guide:
    1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
    2. Initially, let p equal 2, the smallest prime number.
    3. Enumerate the multiples of p by counting to n from 2p in increments of p, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
    4. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
    5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.
3. Pseudocode:
  ```
   Input: an integer n > 1.

   Let A be an array of Boolean values, indexed by integers 2 to n,
   initially all set to true.

   for i = 2, 3, 4, ..., not exceeding √n:
     if A[i] is true:
       for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n:
         A[j] := false.

   Output: all i such that A[i] is true.
  ```
