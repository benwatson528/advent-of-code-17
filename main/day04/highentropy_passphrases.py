def solve_p1(ls) -> int:
    return sum(len(set(l)) == len(l) for l in ls)


def solve_p2(ls) -> int:
    sorted_ls = [["".join(sorted(x)) for x in l] for l in ls]
    return sum(len(set(l)) == len(l) for l in sorted_ls)
