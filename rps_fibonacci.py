def count_rabbits(month: int, litter: int) -> int:
    if month <= 2:
        return 1
    else:
        return count_rabbits(month - 1, litter) + count_rabbits(month - 2, litter) * litter


def count_mortal_rabbits(time: int, litter: int, lifespan: int) -> int:
    if time <= 2:
        return 1
    else:
        rabbits = count_mortal_rabbits(time - 1, litter, lifespan)
        rabbits += count_mortal_rabbits(time - 2, litter, lifespan) * litter
        if time > lifespan:
            rabbits -= count_mortal_rabbits(time - lifespan - 1, litter, lifespan)
        return rabbits

