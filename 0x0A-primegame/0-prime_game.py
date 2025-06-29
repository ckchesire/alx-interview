#!/usr/bin/python3

def sieve_primes_up_to(n):
    """Function to return a list of number of primes up to each i from 0 to n.
    """
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    primes_count = [0] * (n + 1)
    for i in range(1, n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if is_prime[i] else 0)

    return primes_count


def isWinner(x, nums):
    """Function to determine the Prime Game after x rounds.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes_up_to = sieve_primes_up_to(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_moves = primes_up_to[n]
        if prime_moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
