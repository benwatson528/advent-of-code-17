def solve_p1(ls) -> int:
    return sum(int(a) for a, b in list(zip(ls, ls[1:])) + [(ls[-1], ls[0])] if a == b)


def solve_p2(ls) -> int:
    return sum(int(ls[i]) for i in range(len(ls)) if ls[i] == ls[(i + len(ls) // 2) % len(ls)])
