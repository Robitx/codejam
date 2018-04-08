import sys
import itertools


def solve(V, N):
    m = max(V)
    even = V[0:N:2]
    even.sort()
    odd = V[1:N:2]
    odd.sort()
    nV = itertools.zip_longest(even, odd, fillvalue=m)
    nV = itertools.chain.from_iterable(nV)
    i, p = 0, 0
    for c in nV:
        if p > c:
            return i - 1
        p = c
        i += 1
    return "OK"


t = int(input())
for i in range(1, t + 1):
    N = int(input())
    V = list(map(int, sys.stdin.readline().rstrip().split()))[:N]
    print("Case #{}: {}".format(i, solve(V, N)))
