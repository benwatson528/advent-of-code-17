from itertools import combinations


def solve_p1(ls) -> int:
    return sum(max(x for x in l) - min(x for x in l) for l in ls)


def solve_p2(ls) -> int:
    ans = 0
    for l in ls:
        for a, b in combinations(l, 2):
            if a % b == 0:
                ans += a // b
                break
            if b % a == 0:
                ans += b // a
                break
    return ans
