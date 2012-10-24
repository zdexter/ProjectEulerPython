#!/usr/bin/env python

import doctest
import math

def find_largest_palindrome_product(n,verbose=False):
    """Returns largest palindrome made from product of
        two n-digit numbers
    >>> find_largest_palindrome_product(2)
    9009
    """
    palindromes = find_all_palindromes(n,verbose)
    if verbose: print palindromes
    for p in reversed(palindromes):
        # Return the first p for which there are
        #   two n-digit factors
        factor1 = 10**n - 1
        for i in range(factor1, 10**(n-2), -1):
            if p % i == 0 and p / i <= factor1:
                if verbose: print '{} divides {} {} times.'.format(
                    i, p, p/i
                )
                return p

def try_another_digit(myList):
    """Return all possible numbers you can get by
        adding 1 digit to every number in myList
    >>> try_another_digit(["1", "2"])
    ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']
    """
    numbers = "0123456789"
    new_numbers = []
    for entry in myList:
        for num in numbers:
            new_numbers.append(
                entry + num
            )
    return new_numbers

def get_half_palindromes(half_palindrome_length):
    """
    >>> len(get_half_palindromes(3))
    900
    """
    if half_palindrome_length == 1:
        return list("123456789")
    return try_another_digit(get_half_palindromes(half_palindrome_length-1))  
 
def find_all_palindromes(num_factor_digits,verbose=False):
    """Returns all numerical palindromes of length num_factor_digits * 2.
    >>> len(find_all_palindromes(2))
    90
    >>> len(find_all_palindromes(3))
    900
    """
    assert num_factor_digits > 1
    end_digit_choices = "123456789"
     
    palindromes = get_half_palindromes(num_factor_digits)
    palindromes = [int(x + x[::-1]) for x in palindromes]
    if verbose: print 'Found {} {}-digit palindromes.'.format(
        len(palindromes),
        n_original
        )
    return palindromes

if __name__ == '__main__':
    doctest.testmod() 
    print find_largest_palindrome_product(4)
