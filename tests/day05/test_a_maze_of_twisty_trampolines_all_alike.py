import os
from pathlib import Path

from main.day05.a_maze_of_twisty_trampolines_all_alike import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 5


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 356945


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), reduce_three=True) == 10


def test_p2_real():
    assert solve(read_input("data/input.txt"), reduce_three=True) == 28372145

def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [int(x) for x in f.read().splitlines()]
