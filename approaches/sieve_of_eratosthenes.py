import math


def sieve_of_eratosthenes(start, end):
    prime_numbers = []
    boolean_prime_list = [True for _number in range(end + 1)]
    for p in range(2, int(math.sqrt(end) + 1)):
        if boolean_prime_list[p] is True:  # p is prime
            # Update all multiples of p
            for multiple_of_p in range(p * 2, len(boolean_prime_list), p):
                boolean_prime_list[multiple_of_p] = False

    boolean_prime_list[0] = boolean_prime_list[1] = False  # Special case 0 & 1
    for number in range(len(boolean_prime_list)):
        if boolean_prime_list[number] is True and number >= start:
            prime_numbers.append(number)

    return prime_numbers
