from main.day03.spiral_memory import solve


def test_p1_simple():
    assert solve(1) == 0
    assert solve(12) == 3
    assert solve(23) == 2
    assert solve(1024) == 31


def test_p1_real():
    assert solve(361527) == 326
