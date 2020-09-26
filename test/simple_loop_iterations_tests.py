from approaches.simple_loop_iterations import get_prime_numbers_naively, get_prime_numbers_by_root


def test_naive_approach():
    assert get_prime_numbers_naively(0, 5) == [2, 3, 5]
    assert get_prime_numbers_naively(2, 11) == [2, 3, 5, 7, 11]
    assert get_prime_numbers_naively(-5, 11) == [2, 3, 5, 7, 11]
    assert get_prime_numbers_naively(5, 7) == [5, 7]


def test_get_prime_numbers_by_root():
    assert get_prime_numbers_naively(0, 5) == [2, 3, 5]
    assert get_prime_numbers_by_root(2, 11) == [2, 3, 5, 7, 11]
    assert get_prime_numbers_by_root(5, 7) == [5, 7]
