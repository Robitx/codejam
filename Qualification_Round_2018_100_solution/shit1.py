def value(P):
    strength = 1
    damage = 0
    for c in P:
        if c == 'S':
            damage += strength
        else:
            strength *= 2
    return damage, strength / 2


def solve(P, D):
    H = 0
    while True:
        damage, decrease = value(P)
        if "C" not in P:
            return H
        before, after = P.rsplit("C", 1)
        if damage <= D:
            return H
        if damage - decrease * len(after) > D:
            H += len(after)
            P = before + after
            continue
        for c in after:
            H += 1
            damage -= decrease
            if damage <= D:
                return H


t = int(input())
for i in range(1, t + 1):
    D, P = input().split(" ")
    D = int(D)
    if sum(c == 'S' for c in P) > D:
        print("Case #{}: IMPOSSIBLE".format(i))
        continue
    P = P.rstrip("C")
    H = solve(P, D)
    print("Case #{}: {}".format(i, H))
