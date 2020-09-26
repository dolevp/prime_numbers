import math

from utils import two_or_odd_numbers_between


def get_prime_numbers(start, end, is_prime_check):
    if start < 2:
        start = 2

    prime_numbers = []
    for maybe_prime in two_or_odd_numbers_between(start, end):
        if is_prime_check(maybe_prime):
            prime_numbers.append(maybe_prime)

    return prime_numbers


def get_prime_numbers_naively(start, end):
    def prime_check(number):
        for product in two_or_odd_numbers_between(2, number):
            if product != number and number % product == 0:
                return False

        return True

    return get_prime_numbers(start, end, prime_check)


def get_prime_numbers_by_root(start, end):
    def prime_check(number):
        for product in two_or_odd_numbers_between(2, int(math.sqrt(number))):
            if product != number and number % product == 0:
                return False

        return True

    return get_prime_numbers(start, end, prime_check)
