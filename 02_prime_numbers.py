"""Practical 2: Prime number programs."""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 2(a) Check whether n is prime
n = int(input("Enter n: "))
print(n, "is prime" if is_prime(n) else "is not prime")


# 2(b) Generate all prime numbers up to n
n = int(input("\nGenerate primes up to: "))
primes = [x for x in range(2, n + 1) if is_prime(x)]
print("Prime numbers:", primes)


# 2(c) Generate the first n prime numbers
count = int(input("\nHow many prime numbers do you want? "))
first_primes = []
number = 2
while len(first_primes) < count:
    if is_prime(number):
        first_primes.append(number)
    number += 1
print("First", count, "prime numbers:", first_primes)
