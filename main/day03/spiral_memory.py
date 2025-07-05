DIRECTIONS = {">": "^", "^": "<", "<": "v", "v": ">"}
MOVEMENTS = {">": (1, 0), "^": (0, -1), "<": (-1, 0), "v": (0, 1)}
SURROUNDING = [(1, 0), (-1, 0), (1, 1), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1)]


# each square's corner is m^n+2
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
    grid = {(0, 0): 1, (1, 0): 1}
    direction = "^"
    current = (1, 0)
    dist_from_centre = 1
    turn_next = False
    while grid[current] < n:
        next_position = move(*current, *MOVEMENTS[direction])
        if abs(next_position[0]) - dist_from_centre > 0 or abs(next_position[1]) - dist_from_centre > 0:
            if direction == ">" and not turn_next:
                dist_from_centre += 1  # keep moving right one more spot if we're at the corner of the square
                turn_next = True
            else:
                direction = DIRECTIONS[direction]
                turn_next = False
            next_position = move(*current, *MOVEMENTS[direction])

        grid[next_position] = sum(grid.get(move(*next_position, *adjacent), 0) for adjacent in SURROUNDING)
        current = next_position
    return grid[current]


move = lambda x1, y1, x2, y2: (x1 + x2, y1 + y2)

manhattan = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)
