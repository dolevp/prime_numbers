# Prime numbers
Find prime numbers between minimum and maximum values by comparing 3 different approaches and using the fastest one.

Usage: `python find_prime_numbers.py [-h] [--min START] [--max END] [--show_times] [--hide_times]`

Approaches:

* Naive
* Square root (which is a bit of an optimization to the Naive approach)
* Sieve of eratosthenes

_Note: both the Naive approach and its extension are using a bit of an optimization, skipping all even numbers (except for 2 which is prime)_