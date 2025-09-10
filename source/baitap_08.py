# 1.Write a Python function to find the maximum of three numbers.
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max_of_three(10, 25, 15))
# 2.Write a Python function to sum all the numbers in a list.
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_list([1, 2, 3, 4, 5]))
# 3.Write a Python program to reverse a string.
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))
# 4.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n < 0:
        return None  # giai thừa chỉ cho số >= 0
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))
# 5.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))
print(is_prime(20))
# 6.Write a Python function to print
# a) all prime numbers that less than a number (enter prompt keyboard).
def primes_less_than(n):
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes
# b) the first N prime numbers
def first_n_primes(N):
    primes = []
    num = 2
    while len(primes) < N:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
print(primes_less_than(20))
print(first_n_primes(10))
# 7.Write a Python function to check whether a number is "Perfect" or not. Then print all perfect number that less than 1000.
def is_perfect(n):
    if n < 2:
        return False
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n

# in tất cả số hoàn hảo < 1000
for i in range(1, 1000):
    if is_perfect(i):
        print(i)
# 8.Write a Python function to check whether a string is a pangram or not.
# (Note : Pangrams are words or sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog"
import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(s.lower()))

print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("hello world"))  # False
