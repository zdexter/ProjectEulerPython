#!/usr/bin/env python
import math

def naive_largest_prime_factor(num):
	primes = [True for x in range(2,num)]
	prime = 2

	while prime < num:
		if primes[prime-2] == True:
			# Mark multiples as nonprime
			multiple = prime + prime
			while multiple < num:
				primes[multiple-2] = False
				multiple += prime
		prime += 1

	x = len(primes) - 1
	for x in range(len(primes) - 1, 0, -1):
		if primes[x - 2] == True and num % x == 0:
			return x

def largest_prime_factor(num):
	# Observation: if a*b=n, one factor will always be <= sqrt(n).
	# 	So the largest prime factor will have another factor <= sqrt(n).
	#	We can divide num by that other factor to get the prime factor.
	for i in range(2, int(math.floor(math.sqrt(num)))):
		if num % i == 0: # num can be divided and is therefore nonprime
			return max(i, largest_prime_factor(num / i))
	return num # The number called with was prime

if __name__ == '__main__':
	assert largest_prime_factor(21) == 7
	assert largest_prime_factor(13195) == 29
	print largest_prime_factor(600851475143)