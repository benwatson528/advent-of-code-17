DIRECTIONS = {">": "^", "^": "<", "<": "v", "v": ">"}
MOVEMENTS = {">": (1, 0), "^": (0, -1), "<": (-1, 0), "v": (0, 1)}


def solve_p1(x) -> int:
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


def solve_p2(n) -> int:
    grid = {}
    square_val = 1
    grid[(0, 0)] = square_val
    direction = ">"
    x = 1
    y = 0
    square_size = 1
    while square_val < n:
        grid[(x, y)] = sum(grid.get(move(x, y, *a), 0) for a in [(1, 0), (-1, 0), (0, 1), (0, -1)])

        if direction == ">":
            if move(x, y, *MOVEMENTS[direction])[0] > square_size:
                direction = DIRECTIONS[direction]

    return square_val


move = lambda x1, y1, x2, y2: (x1 + x2, y1 + y2)
