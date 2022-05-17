# Ex 1
from asyncio import FastChildWatcher


def delta(t) :
    i, nT = 1, [t[0]]
    while i < len(t):
        nT.append(t[i] - t[i-1])
        i+=1
    return print(nT)
delta([1000, 800, 802, 1000, 1003])
delta([42])

# Ex 2