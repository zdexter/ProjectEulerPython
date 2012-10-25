#!/usr/bin/env python

def min_evenly_divisible_by(max_num):
    """Return the small positive number that is evenly
        divisible by all of the numbers from 1 to max_num.
    """
    num_to_test = max_num
    while not is_divisible_by_range(max_num, num_to_test):
        num_to_test += max_num # final val must be mult of max_num 
    return num_to_test

def is_divisible_by_range(max_num, num_to_test):
    for x in range(max_num, 1, -1):
        if num_to_test % x != 0:
            return False
    return True

if __name__ == '__main__':
    print min_evenly_divisible_by(20)
