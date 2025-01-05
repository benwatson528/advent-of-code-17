def solve(ls, reduce_three=False) -> int:
    i = 0
    num_steps = 0
    while i < len(ls):
        last_val = ls[i]
        ls[i] += -1 if reduce_three and last_val >= 3 else 1
        i += last_val
        num_steps += 1

    return num_steps
