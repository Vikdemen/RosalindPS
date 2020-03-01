from rps.dynamic_programming_problems.rabbits_and_recurrence_relations import count_rabbits


def test_count_rabbits():
    sample_values = ['5 3']
    expected_rabbits = 19
    rabbits = int(count_rabbits(sample_values))
    assert rabbits == expected_rabbits
