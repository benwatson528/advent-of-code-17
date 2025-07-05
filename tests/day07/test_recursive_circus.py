import os
from collections import defaultdict
from pathlib import Path

from main.day07.recursive_circus import solve_p1


def test_p1_simple():
    assert solve_p1(*read_input("data/test_input.txt")) == "tknk"


def test_p1_real():
    assert solve_p1(*read_input("data/input.txt")) == "dgoocsw"


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        nodes = defaultdict(list)
        weights = {}
        for l in f.read().splitlines():
            name = l.split(" ")[0]
            weights[name] = l.split("(")[1].split(")")[0]
            nodes[name] = l.split(" -> ")[1].split(", ") if " -> " in l else []
    return nodes, weights