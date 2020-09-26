import argparse
import timeit

import approaches
from config.settings import TIMEIT_NUMBER_OF_CALLS, DEFAULT_PRIME_NUMBERS_START, DEFAULT_PRIME_NUMBERS_END, \
    DEFAULT_SHOW_TIMES

"""
Simple python script to find prime numbers from a start_number to an end_number & compare 
different methods for doing so.
It uses lists instead of generators solely for time measuring purposes;
Replacing the lists with generators will be better in terms of memory management and readability.
"""


def get_approaches():
    return {name: val for name, val in approaches.__dict__.items() if callable(val)}


def get_average_execution_time(function_name, start, end):
    function_call_string = f'{function_name}({start}, {end})'
    function_import_string = f'from approaches import {function_name}'

    total_time_in_seconds = timeit.Timer(
        function_call_string,
        setup=function_import_string
    ).timeit(number=TIMEIT_NUMBER_OF_CALLS)

    return total_time_in_seconds / TIMEIT_NUMBER_OF_CALLS


def print_primes_from_fastest_approach(start, end, show_timeit_results):
    time_by_function = {}
    for function_name, _ in get_approaches().items():
        average_time = get_average_execution_time(function_name, start, end)
        time_by_function[function_name] = average_time
        if show_timeit_results is True:
            print(f"{function_name} took {average_time}(s) on average")

    fastest_approach_name = min(time_by_function, key=time_by_function.get)
    fastest_approach = approaches.__dict__[fastest_approach_name]
    primes = [str(prime) for prime in fastest_approach(start, end)]
    print("\n".join(primes))
    return time_by_function


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find prime numbers between 2 numbers')
    parser.add_argument('--min', dest='start', type=int,
                        help=f'Find prime numbers starting from this one.'
                             f' (default: {DEFAULT_PRIME_NUMBERS_START})',
                        default=DEFAULT_PRIME_NUMBERS_START)

    parser.add_argument('--max', dest='end', type=int,
                        help=f'Stop the search when you get to this number.'
                             f' (default: {DEFAULT_PRIME_NUMBERS_END})',
                        default=DEFAULT_PRIME_NUMBERS_END)

    parser.add_argument('--show_times', help='Show the time it took for each and every approach',
                        dest='show_timeit_results', action='store_true')

    parser.add_argument('--hide_times', help='Hide the time it took for each and every approach',
                        dest='show_timeit_results', action='store_false')

    parser.set_defaults(show_timeit_results=DEFAULT_SHOW_TIMES)

    args = parser.parse_args()
    print_primes_from_fastest_approach(args.start, args.end, args.show_timeit_results)
