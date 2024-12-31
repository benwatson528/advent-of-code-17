import os
from pathlib import Path

from main.day02.corruption_checksum import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input_p1.txt")) == 18


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 54426


def test_p2_simple():
    assert solve_p2(read_input("data/test_input_p2.txt")) == 9


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 333


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return list([int(x) for x in row.split()] for row in f)
