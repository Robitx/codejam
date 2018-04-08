import sys
import math


def eprint(*args):
    f = open("shit3.txt", "a")
    f.write(" ".join(list(map(str, args))) + "\n")
    f.close()


def fprint(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()


t = int(input())
GRID = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
for _ in range(1, t + 1):
    A = int(input())
    s = int(math.sqrt(A))
    if s * s >= A:
        X, Y = s, s
    elif s * (s + 1) >= A:
        X, Y = s, s + 1
    else:
        X, Y = s + 1, s + 1
    AREA = [[0] * (Y + 1) for _ in range(0, X + 2)]
    NS = {(x, y): 0 for x in range(2, X) for y in range(2, Y)}
    # eprint("=" * 80)
    while True:
        N = min(NS.items(), key=lambda x: x[1])[0]

        fprint("{} {}".format(N[0], N[1]))

        x, y = map(int, input().split())
        # eprint(x, y)

        if x == -1 and y == -1:
            sys.exit()
        if x == 0 and y == 0:
            break
        if AREA[x][y]:
            continue
        AREA[x][y] = 1
        for g in GRID:
            gc = (g[0] + x, g[1] + y)
            if gc not in NS:
                continue
            NS[gc] += 1
