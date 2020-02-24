def memoization(f):
    """
    :param f:
    :return:
    Remembers the previously computed values
    """
    cache = {}

    def func(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return func


@memoization
def count_rabbits(month: int, litter: int) -> int:
    if month <= 2:
        return 1
    else:
        return count_rabbits(month - 1, litter) + count_rabbits(month - 2, litter) * litter


@memoization
def count_mortal_rabbits(time: int, lifespan: int) -> int:
    """
    :param time:
    :param lifespan:
    :return:
    We consider that in that problem there is only 1 child pair in litter
    """
    # returning 0 when time <= 0 gives wrong results
    if time <= 2:
        return 1
    else:
        rabbits = count_mortal_rabbits(time - 1, lifespan)
        rabbits += count_mortal_rabbits(time - 2, lifespan)
        if time > lifespan:
            rabbits -= count_mortal_rabbits(time - lifespan - 1, lifespan)
        return rabbits

