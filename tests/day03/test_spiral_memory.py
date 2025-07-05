from main.day03.spiral_memory import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(1) == 0
    assert solve_p1(12) == 3
    assert solve_p1(23) == 2
    assert solve_p1(1024) == 31


def test_p1_real():
    assert solve_p1(361527) == 326


def test_p2_real():
    assert solve_p2(361527) == 363010
