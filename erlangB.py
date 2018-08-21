import numpy as np

class Erlang():

    def __init__(self, call_rate, call_time):
        self.call_rate = call_rate
        self.call_time = call_time
        self.E = call_rate*call_time

    def __str__(self):
        return (f'Call Rate: {self.call_rate} \n' +
                f'Call Time: {self.call_time} \n' +
                f'E: {self.E}')

    def B(self, n):
        '''
        Finds the probability of blockage with
        the Erlang B Function.
        '''
        top = (self.E**n)/ (np.prod(range(1,n+1)))
        x = [self.E**i for i in range(0,n+1)]
        y = [np.prod(range(1,j+1)) for j in range (0,n+1)]
        bottom = np.sum(np.divide(x,y))
        return top/bottom

    def C(self, n):
        '''
        Finds the probability of a
        delay with the Erlang C Function
        '''
        top = n*self.B(n)
        bottom = n - self.E*(1 - self.B(n))
        # Just so we don't divide by zero:
        if n == 0:
            return 1
        # The probability can't be bigger than 1:
        else:
            return np.minimum(1, top/bottom)

class FindErlang():

    def __init__(self):
        pass

    def findN_B(self, B, E):
        '''
        Finds N, given B and E,
        using the Erlang B Function
        '''
        n = 1
        while True:
            x = Erlang(E,1)
            B_found = x.B(n)
            if B_found <= B:
                return n, B_found
            else:
                n += 1

    def findE_B(self, n, B):
        '''
        Finds E, given B and n,
        using the Erlang B function
        '''
        E0 = 1
        eps = 0.001
        E1 = 0

        while True:
            x = Erlang(E0,1)
            B_found = x.B(n)
            if B_found - B >= eps:
                E2 = E0
                break
            else:
                E0 += 1

        while True:
            x = Erlang(E2,1)
            B_found = x.B(n)
            step = abs(E2 - E1)

            if B_found - B >= eps:
                inter = E2
                E2 -= step/2
                E1 = inter
            elif B_found - B <= -eps:
                inter = E2
                E2 += step/2
                E1 = inter
            else:
                return E2

    def table_B(self, n_max, B):
        dict_erl = {}
        for k in range(1, n_max+1):
            E_B = [round(FindErlang().findE_B(k,i),2) for i in B]
            dict_erl[str(k)] = {i:j for i,j in zip(B,E_B)}

        return dict_erl

    def findE_B_grad(self, n, B):
        '''
        Finds E, given B and n,
        using the Erlang B function
        '''
        alpha = 0.5
        eps = 0.001
        E = 1
        while True:
            x = Erlang(E,1)
            B_found = x.B(n)
            error = abs(B_found - B)
            # Is B_found within the given error?
            if error <= eps:
                return E
            # Calculating the Derivative
            top = E**(n-1)/(np.prod(range(1,n)))
            x = [E**(i-1) for i in range(1,n+1)]
            y = [np.prod(range(1,j+1)) for j in range (1,n+1)]
            bottom = np.sum(np.divide(x,y))
            der = (B_found - B) * (top/bottom)
            # Gradient Descent
            E -= alpha*der
