#!/usr/bin/env python

def find_largest_palindrome_product(n):
    """Returns largest palindrome made from product of
        two n-digit numbers
    """
    palindromes = find_all_palindromes(n*2)
    print palindromes
    for p in reversed(palindromes):
        # Return the first p for which there are
        #   two n-digit factors
        factor1 = 10**n - 1
        for i in range(factor1, 10**(n-2), -1):
            if p % i == 0 and p / i <= factor1:
                print '{} divides {} {} times.'.format(
                    i, p, p/i
                )
                return p
    
def find_all_palindromes(n_original):
    """Returns all n-digit numerical palindromes.
    """
    assert n_original > 1
    import math
    n = int(math.floor(n_original / 2))
    end_digit_choices = range(1, 10)
    num_middle_digits = n - 1
    middle_digit_choices = range(10)
    palindromes = []
    
    for c in end_digit_choices:
        palindrome = c * 10**(n-1)
        for x in range(num_middle_digits):
            for d in middle_digit_choices:
                palindromes.append(
                    palindrome + d * 10**(x)
                )
    palindromes = [int(str(x) + str(x)[::-1]) for x in palindromes]
    print 'Found {} {}-digit palindromes.'.format(
        len(palindromes),
        n_original
        )
    return palindromes

if __name__ == '__main__':
    assert find_largest_palindrome_product(2) == 9009
    print find_largest_palindrome_product(3)
