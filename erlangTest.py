import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from erlangB import Erlang
from erlangB import FindErlang
import csv

# # Tests
#
# k = FindErlang()
# print(k.findE_B(3,0.1))
#
# # Plotting B x E graph
#
# E_x = [i/10 for i in range(1,101)]
# B_E = [Erlang(i/10,1).B(2) for i in range(1,101)]
#
# fig, ax = plt.subplots()
# ax.plot(E_x,B_E)
# ax.grid()
# ax.set(xlabel = 'E', ylabel = 'B(E)')
# plt.show()

# Erlang Table

B = [0.01,0.012,0.015,0.02,0.03,0.05,
     0.07,0.1,0.15,0.2,0.3,0.4,0.5]
G = FindErlang().table_B(6,B)

keys = B

G_list = [G[str(i)] for i in G]

with open('test.csv', 'w') as f:
    f.write(' ,')
    for j in B:
        f.write(f'{j},')
    f.write('\n')

    n = 1
    for i in G_list:
        f.write(f'{n},')
        n += 1
        for key in i.keys():
            f.write(f'{i[key]},')
        f.write('\n')

import time

tic1 = time.time()
T = FindErlang().findE_B_grad(7,0.05)
toc1 = time.time()
tic2 = time.time()
T2 = FindErlang().findE_B(7,0.05)
toc2 = time.time()
print(T)
print(T2)
print(toc1-tic1)
print(toc2-tic2)
