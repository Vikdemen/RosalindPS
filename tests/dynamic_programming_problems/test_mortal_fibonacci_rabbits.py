from rps.dynamic_programming_problems.mortal_fibonacci_rabbits import count_mortal_rabbits


def test_count_mortal_rabbits():
    values = ['6 3']
    expected_rabbits = 4
    rabbits = count_mortal_rabbits(values)
    assert rabbits == expected_rabbits
