from approaches.sieve_of_eratosthenes import sieve_of_eratosthenes


def test_sieve():
    assert sieve_of_eratosthenes(0, 5) == [2, 3, 5]
    assert sieve_of_eratosthenes(2, 11) == [2, 3, 5, 7, 11]
    assert sieve_of_eratosthenes(5, 7) == [5, 7]
