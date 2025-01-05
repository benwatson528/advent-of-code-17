def solve_p1(bank) -> int:
    return len(redistribute(bank)[0])



def solve_p2(bank) -> int:
    repeated = redistribute(bank)[1]
    return len(redistribute(repeated)[0])



def redistribute(bank):
    seen = set()
    while tuple(bank) not in seen:
        seen.add(tuple(bank))
        biggest = max(bank)
        biggest_idx = bank.index(biggest)
        bank[biggest_idx] = 0
        i = 1
        while i <= biggest:
            bank[(biggest_idx + i) % len(bank)] += 1
            i += 1
    return seen, bank


