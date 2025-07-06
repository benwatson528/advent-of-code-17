from dataclasses import dataclass
from typing import List


def solve_p1(discs, _) -> str:
    return list(set(discs.keys()).difference(set(x for xs in discs.values() for x in xs)))[0]


# def solve_p2(discs, weights) -> int:
#     root_name = solve_p1(discs, weights)
#     root_node = Node(root_name, weights[root_name], children=[])
#     build_tree(root_node, discs, weights)
#     current = root_node
#     while current.children:
#         summed = {child.name: sum_subtree(child, weights) for child in current.children}
#         c = Counter(summed.values())
#         odd_one_out = list(c.keys())[list(c.values()).index(1)]
#         target = list(set(summed.values()) - {odd_one_out})[0]
#         odd_key_out = list(summed.keys())[list(summed.values()).index(odd_one_out)]
#         current = get_child_by_name(current, odd_key_out)
#         print()
#     return weights[odd_key_out] - abs(odd_one_out - target)


def build_tree(current, discs, weights):
    for child_name in discs[current.name]:
        child = Node(child_name, weights[child_name], [])
        current.children.append(child)
        build_tree(child, discs, weights)


def get_child_by_name(current, child_name):
    for child in current.children:
        if child.name == child_name:
            return child
    return None


sum_subtree = lambda current, weights: weights[current.name] + sum(
    sum_subtree(child, weights) for child in current.children)


@dataclass(frozen=True)
class Node:
    name: str
    weight: int
    children: List
