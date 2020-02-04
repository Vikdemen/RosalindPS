from rps.dynamic_programming import fibonacci as fib


def test_mortal_rabbits():
    time = 6
    lifespan = 3
    output = 4
    result = fib.count_mortal_rabbits(time, lifespan)
    assert result == output