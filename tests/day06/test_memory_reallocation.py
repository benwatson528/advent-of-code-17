import re

from main.day06.memory_reallocation import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("0  2  7  0")) == 5


def test_p1_real():
    assert solve_p1(
        read_input("4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3")) == 6681


def test_p2_simple():
    assert solve_p2(read_input("0  2  7  0")) == 4


def test_p2_real():
    assert solve_p2(
        read_input("4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3")) == 2392


def read_input(i):
    return [int(x) for x in re.findall("\d+", i)]
