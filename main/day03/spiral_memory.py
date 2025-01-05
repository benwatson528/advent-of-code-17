def solve(x) -> int:
    if x == 1:
        return 0

    lower_square = 1
    while True:
        if lower_square * lower_square > x:
            lower_square -= 1
            break
        lower_square += 1

    if lower_square % 2 == 0:
        lower_square -= 1

    square_start = pow(lower_square, 2)
    square_end = pow(lower_square + 2, 2)
    middles = [square_start + (((square_end - square_start) // 8) * n) for n in range(1, 8, 2)]
    closest_middle = min(middles, key=lambda n: abs(n - x))
    return abs(x - closest_middle) + (lower_square // 2) + 1
