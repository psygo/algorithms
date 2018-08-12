import itertools
import math

def solve_51(N,primes_N,len_51):
    '''
    Solving Problem 51 of Project Euler's site
    Check up to including N, with the number of
    primes being len_51.
    '''

    progress = [l for l in range(1,101)]

    # Eliminating the first 56000 numbers because they
    # have already been checked


    # Now we check for the problem
    # We will need to check for every prime number:
    for n in primes_N:

        # We must have a list version of the number
        list_of_number = [int(k) for k in str(n)]

        # Index to create the combinations
        indexy = []
        for iteration in range(0,len(list_of_number)):
            indexy.append(iteration)

        # Creates a dictionary with the index and the digit
        dict_of_number = {x:y for x,y in
                          zip(range(0,len(list_of_number)),
                          list_of_number)}

        # Get the list of combinations for the indexes
        comb = []
        for L in range(1, len(indexy)):
            for subset in itertools.combinations(indexy, L):
                comb.append(subset)
        comb_list = [list(i) for i in comb]

        prime_collection = []
        new_numb_dict = {a:b for a,b in
                         zip(dict_of_number.keys(),
                         dict_of_number.values())}

        #Calculating Progress:
        # progress_now = math.ceil((n/N)*100)
        # if progress_now in progress:
        #     print(f"Progress solve_51: {progress_now}%",end="\r")
        #     progress.remove(progress_now)
        print(f"Number being evaluated: {n}",end="\r")

        # Main Loop:
        for i in range(0,len(comb_list)):

            prime_collection = []

            # Replacing the numbers according to the combinations
            for j in range(0,10):
                for k in comb_list[i]:
                    new_numb_dict[k] = j

                # Transform into number
                list_new_numb = [i for i in new_numb_dict.values()]
                new_numb = int("".join(map(str,list_new_numb)))

                # Check if prime
                # Need to exclude numbers with leading '0'
                if new_numb in primes_N and len(str(new_numb)) == len(str(n)):
                    prime_collection.append(new_numb)

                new_numb_dict = {a:b for a,b in
                                 zip(dict_of_number.keys(),
                                 dict_of_number.values())}

            # Need to include the original number and exclude copies
            prime_collection = list(set(prime_collection))

            # Length of the prime collection searched
            if len(prime_collection) >= len_51:
                print('\n',n)
                print(comb_list[i])
                print(prime_collection)
                return

    print("Sad! No numbers found to solve the problem!")
