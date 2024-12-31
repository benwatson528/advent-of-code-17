import os
from pathlib import Path

from main.day01.inverse_captcha import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1("1122") == 3
    assert solve_p1("1111") == 4
    assert solve_p1("1234") == 0
    assert solve_p1("91212129") == 9


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 1097


def test_p2_simple():
    assert solve_p2("1212") == 6
    assert solve_p2("1221") == 0
    assert solve_p2("123425") == 4
    assert solve_p2("123123") == 12
    assert solve_p2("12131415") == 4


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 1188


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().strip()
