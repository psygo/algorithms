import math

def eratos(N):
    '''
    Look for the prime numbers
    up to, including, N
    eratos(N)
    '''
    numbers = []

    for i in range(1,N+1):
        numbers.append(i)

    progress_eratos = [l for l in range(1,101)]
    top_range = math.ceil(N**0.5)+1

    for i in range(2,top_range):

        # Calculating Progress:
        progress_now = math.ceil((i/top_range)*100)
        if progress_now in progress_eratos:
            print(f"Progress Eratos: {progress_now}%",end="\r")
            progress_eratos.remove(progress_now)

        for j in range(i**2,N+1,i):
            try:
                numbers.remove(j)
            except:
                continue

    return numbers
