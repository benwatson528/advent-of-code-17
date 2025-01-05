import os
from pathlib import Path

from main.day04.highentropy_passphrases import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 2


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 337


def test_p2_simple():
    assert solve_p2(read_input("data/test_input_p2.txt")) == 3


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 231


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [x.split() for x in f.read().splitlines()]
