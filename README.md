# What's inside this Repo?

This is a collection of famous algorithms, which I mainly used to learn more about Python and programming. For more info, visit [fanaro.com.br](http://fanaro.com.br/).

Among them, you will find:

  1. Sieve of Eratosthenes
  1. Dijkstra's Shortest Path
  1. Solution to Problem 51 from Project Euler
  1. Erlang's Queueing B Function and Table Generator

## Sieve of Eratosthenes

This is an ancient and simple algorithm created by Eratosthenes of Cyrene, a Greek mathematician. It is one of the most efficient ways of generating primes.

The core of the algorithm is to scratch out all multiples of primes. For example, we first scratch out all of the multiples of 2, then of 3, then of 5, etc. Naturally, the only numbers remaining in the list will be primes.

Two classic improvements have also been added: firstly, you need only to check numbers above and including the square of prime being checked, because the numbers below it will either have been already scratched out by prior primes or are primes; and, secondly, you only need to check multiples of numbers up to the root of the biggest number in the list, since the numbers above it will be checked during the algorithm.

There are other more modern improvements that could be implemented, but, for the sake of simplicity, I'll leave it like this. For more info, you can check [Wikipedia](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).

## Dijkstra's Shortest Path

Dijkstra's algorithm calculates the shortest path from one node to another within a graph. It is a greedy and very simple algorithm which updates the shortest path every time it checks a new node.

Its implementation usually is usually coupled with special properties (like only checking for roads if you want to do an interstate route search) of the graph/map to lower the complexity of the method, since checking every node can oftentimes be too computationally expensive. In this file, though, only the basic algorithm is implemented. For more info, check [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).

## Solution to Problem 51 from Project Euler

Problem 51 is found [here](https://projecteuler.net/archives). It asks you to find the family of 8 numbers containing only primes which have replaceable digits that also yield other primes. For example, 56003 is a prime which can have its 0-digits replaced by others and still yield 6 primes: 56113, 56333, 56433, 56663, 56773 and 56773.

The solution found in this repo (with the files `solve_51.py` and `answer_51.py`) uses pure brute force and can be very inefficient. It first finds all the possible combinations of digits to be replaced and then tries to see if those can make a family of primes by replacing them with other ones. For example, the number of combinations of digits of a 5-digit number would be ![equation](http://latex.codecogs.com/gif.latex?C_%7B5%2C5%7D%20&plus;%20C_%7B5%2C4%7D%20&plus;%20C_%7B5%2C3%7D%20&plus;%20C_%7B5%2C2%7D%20&plus;%20C_%7B5%2C1%7D).

As mentioned before this is very expensive. A first and obvious improvement would be to scratch out the primes which were checked to have families too small to solve the problem. Other improvements use several properties of prime numbers which I didn't know, you can take a look at them [here](https://blog.dreamshire.com/project-euler-51-solution/).

Another detail worth mentioning is that using the *Sieve of Eratosthenes* to solve this problem may not be a good use of your computer, since primes up to 1 million (you always need primes up to ![equation](http://latex.codecogs.com/gif.latex?10%5Ex) to calculate the families for numbers with ![equation](http://latex.codecogs.com/gif.latex?x) digits) are required. I advise you to use a file with the calculated primes, which can also be found inside the repo.

## Erlang's Queueing B Function and Table Generator

The Erlang B function yields the probability of blockage in a queueing system, given n and the normalized traffic ![equation](http://latex.codecogs.com/gif.latex?E%20%3D%20Call%20%5C%20Rate%20%5Ctimes%20Call%20%5C%20Time). The formulas can be found [here](https://en.wikipedia.org/wiki/Erlang_(unit)#Erlang_B_formula) and an alternative explanation [here](http://abstractmicro.com/erlang/helppages/mod-b.htm).

Usually, though, you actually have B and n and want to find the traffic E; or you have B and E and want to find n. This used to be done with [tables](http://2.bp.blogspot.com/-iaCH0pVu1iE/Uoh7AZydqSI/AAAAAAAAAFM/ur6uipfGaxc/s1600/Erlang+B.PNG) but nowadays you can implement it in code, and that's what we have here.

To find n, a brute force search was implemented, which finds an n with a smaller or equal probability of blockage given a certain normalized traffic.

To find E, a more refined algorithm can be implemented, which uses gradient descent, since the derivative of ![equation](http://latex.codecogs.com/gif.latex?B%28E%2Cn%29) is a continuous function (it could kind of also be done for the other case...).

![equation](http://latex.codecogs.com/gif.latex?%5Cbegin%7Balign*%7D%20%26Cost%20%3D%20%5Cfrac%7B1%7D%7B2%7D%20%28%5Chat%7BB%7D%20-%20B%29%5E2%20%5C%5C%20%26%5Cfrac%7B%5Cpartial%20Cost%7D%7B%5Cpartial%20E%7D%20%3D%20%28%5Chat%7BB%7D%20-%20B%29%20%5Ccdot%20%5Cfrac%7B%5Cpartial%20%5Chat%7BB%7D%20%28E%2Cn%29%7D%7B%5Cpartial%20E%7D%20%3D%20%5Cfrac%7B%28%5Chat%7BB%7D%20-%20B%29%20%5Cfrac%7BE%5E%7Bn-1%7D%7D%7B%28n-1%29%21%7D%7D%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%5Cfrac%7BE%5E%7Bi-1%7D%7D%7B%28i-1%29%21%7D%7D%20%5C%5C%20%26E%28i%29%20%3D%20E%28i-1%29%20-%20%5Calpha%20%5Cfrac%7B%5Cpartial%20Cost%7D%7B%5Cpartial%20E%7D%20%5Cend%7Balign*%7D)

I've also implemented a less clever search - and an Erlang Table Generator - which only halfs the search interval every time it gets closer to the target. This seems to be a better implementation actually, since it's much less computationally expensive, and it also doesn't have convergence problems due to a learning rate.
