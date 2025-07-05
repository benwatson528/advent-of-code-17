def solve_p1(nodes, weights) -> str:
    return list(set(nodes.keys()).difference(set(x for xs in nodes.values() for x in xs)))[0]
