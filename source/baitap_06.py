# 1. Write a Python program to sum all the items in a list.
def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4]))
# 2. Write a Python program to multiply all the items in a list.
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

print(multiply_list([1, 2, 3, 4]))
# 3. Write a Python program to get the largest number from a list.
def max_in_list(lst):
    return max(lst)

print(max_in_list([1, 2, 99, 3, 4]))
# 4. Write a Python program to get the smallest number from a list.
def min_in_list(lst):
    return min(lst)

print(min_in_list([1, 2, 99, 3, 4]))
# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
def count_strings(lst):
    count = 0
    for s in lst:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

sample_list = ['abc', 'xyz', 'aba', '1221']
print(count_strings(sample_list))  # Expected: 2
# 6. Write a Python program to get a list, sorted in increasing order by the last
def sort_tuple_list(lst):
    return sorted(lst, key=lambda x: x[-1])

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_tuple_list(sample_list))
# 7. Write a Python program to remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
# 8. Write a Python program to check if a list is empty or not
def is_list_empty(lst):
    return len(lst) == 0

print(is_list_empty([]))       # True
print(is_list_empty([1, 2]))   # False
# 9. Write a Python program to clone or copy a list.
def clone_list(lst):
    return lst.copy()

sample = [1, 2, 3, 4]
print(clone_list(sample))  # [1, 2, 3, 4]
# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
def words_longer_than_n(words, n):
    return [word for word in words if len(word) > n]

sample_words = ["hello", "to", "world", "a", "python"]
print(words_longer_than_n(sample_words, 3))
# ['hello', 'world', 'python']
# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def has_common_member(list1, list2):
    return any(item in list1 for item in list2)

print(has_common_member([1, 2, 3], [4, 5, 2]))  # True
print(has_common_member([1, 2], [3, 4]))        # False
# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
def remove_specific_elements(lst):
    return [lst[i] for i in range(len(lst)) if i not in (0, 4, 5)]

sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_specific_elements(sample))
# ['Green', 'White', 'Black']
# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
def generate_3d_array():
    return [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

array = generate_3d_array()
print(array)  # sẽ in ra cấu trúc 3x4x6 toàn '*'
# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
def remove_even_numbers(lst):
    return [x for x in lst if x % 2 != 0]

sample = [1, 2, 3, 4, 5, 6, 7]
print(remove_even_numbers(sample))
# [1, 3, 5, 7]
# 15. Write a Python program to shuffle and print a specified list.
import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

sample = [1, 2, 3, 4, 5]
print(shuffle_list(sample))
# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
def first_last_squares():
    squares = [x**2 for x in range(1, 31)]
    return squares[:5] + squares[-5:]

print(first_last_squares())
# [1, 4, 9, 16, 25, 676, 729, 784, 841, 900]
# 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_primes(lst):
    return all(is_prime(n) for n in lst)

print(all_primes([0, 3, 4, 7, 9]))   # False
print(all_primes([3, 5, 7, 13]))     # True
print(all_primes([1, 5, 3]))         # False
# 18. Write a Python program to generate all permutations of a list in Python.
import itertools

def list_permutations(lst):
    return list(itertools.permutations(lst))

print(list_permutations([1, 2, 3]))
# [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]
# 19. Write a Python program to calculate the difference between the two lists.
def list_difference(list1, list2):
    return list(set(list1) - set(list2))

print(list_difference([1, 2, 3, 4], [2, 4]))
# [1, 3]
# 20. Write a Python program to access the index of a list.
def access_indexes(lst):
    for i, val in enumerate(lst):
        print(f"Index {i}: {val}")

sample = ['a', 'b', 'c']
access_indexes(sample)
# Index 0: a
# Index 1: b
# Index 2: c
# 21. Write a Python program to convert a list of characters into a string.
def chars_to_string(char_list):
    return ''.join(char_list)

print(chars_to_string(['P', 'y', 't', 'h', 'o', 'n']))
# "Python"
# 22. Write a Python program to find the index of an item in a specified list.
def find_index(lst, item):
    return lst.index(item) if item in lst else -1

sample = ['Red', 'Green', 'Blue']
print(find_index(sample, 'Green'))  # 1
print(find_index(sample, 'Pink'))   # -1
# 23. Write a Python program to flatten a shallow list.
def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

sample = [[1, 2], [3, 4], [5, 6]]
print(flatten_list(sample))
# [1, 2, 3, 4, 5, 6]
# 24. Write a Python program to append a list to the second list.
def append_lists(list1, list2):
    return list1 + list2

print(append_lists([1, 2, 3], [4, 5, 6]))
# [1, 2, 3, 4, 5, 6]
# 25. Write a Python program to select an item randomly from a list.
import random

def random_choice(lst):
    return random.choice(lst)

print(random_choice([10, 20, 30, 40, 50]))
# 26. Write a Python program to check whether two lists are circularly identical.
def circularly_identical(list1, list2):
    return len(list1) == len(list2) and ''.join(map(str, list2)) in ''.join(map(str, list1*2))

print(circularly_identical([1, 2, 3], [2, 3, 1]))  # True
print(circularly_identical([1, 2, 3], [3, 2, 1]))  # False
# 27. Write a Python program to find the second smallest number in a list.
def second_smallest(lst):
    unique_sorted = sorted(set(lst))
    return unique_sorted[1] if len(unique_sorted) >= 2 else None

print(second_smallest([1, 2, 3, 4, 5]))  # 2
# 28. Write a Python program to find the second largest number in a list.
def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None

print(second_largest([1, 2, 3, 4, 5]))  # 4
# 29. Write a Python program to get unique values from a list.
def unique_values(lst):
    return list(set(lst))

print(unique_values([1, 2, 2, 3, 4, 4, 5]))
# [1, 2, 3, 4, 5]
# 30. Write a Python program to get the frequency of elements in a list.
from collections import Counter

def frequency(lst):
    return dict(Counter(lst))

print(frequency([1, 2, 2, 3, 3, 3, 4]))
# {1: 1, 2: 2, 3: 3, 4: 1}
# 31. Write a Python program to count the number of elements in a list within a specified range.
def count_in_range(lst, min_val, max_val):
    return sum(min_val <= x <= max_val for x in lst)

sample = [10, 20, 30, 40, 50, 60]
print(count_in_range(sample, 20, 50))
# 3 (20, 30, 40)
# 32. Write a Python program to check whether a list contains a sublist.
def contains_sublist(lst, sublist):
    n, m = len(lst), len(sublist)
    for i in range(n - m + 1):
        if lst[i:i+m] == sublist:
            return True
    return False

print(contains_sublist([1, 2, 3, 4], [2, 3]))  # True
print(contains_sublist([1, 2, 3, 4], [3, 5]))  # False
# 33. Write a Python program to generate all sublists of a list.
def all_sublists(lst):
    sublists = []
    for i in range(len(lst)+1):
        for j in range(i+1, len(lst)+1):
            sublists.append(lst[i:j])
    return sublists

print(all_sublists([1, 2, 3]))
# [[1], [1,2], [1,2,3], [2], [2,3], [3]]
# 34. Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit+1)
    primes[0], primes[1] = False, False
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p*p, limit+1, p):
                primes[i] = False
        p += 1
    return [i for i, is_prime in enumerate(primes) if is_prime]

print(sieve_of_eratosthenes(30))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
def concat_list_with_range(lst, n):
    return [x + str(i) for i in range(1, n+1) for x in lst]

print(concat_list_with_range(['p', 'q'], 5))
# ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
# 36. Write a Python program to get a variable with an identification number or string.
x = "Hello"
print("ID of variable x:", id(x))

y = 100
print("ID of variable y:", id(y))
# 37. Write a Python program to find common items in two lists.
def common_items(list1, list2):
    return list(set(list1) & set(list2))

print(common_items([1, 2, 3, 4], [3, 4, 5, 6]))
# [3, 4]
# 38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
def swap_pairs(lst):
    new_list = lst[:]
    for i in range(0, len(new_list)-1, 2):
        new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
    return new_list

print(swap_pairs([0,1,2,3,4,5]))
# [1, 0, 3, 2, 5, 4]
# 39. Write a Python program to convert a list of multiple integers into a single integer.
def list_to_integer(lst):
    return int(''.join(map(str, lst)))

print(list_to_integer([11, 33, 50]))
# 113350
# 40. Write a Python program to split a list based on the first character of a word.
from collections import defaultdict

def split_by_first_char(words):
    groups = defaultdict(list)
    for word in words:
        groups[word[0]].append(word)
    return dict(groups)

sample = ["apple", "banana", "apricot", "blueberry", "cherry"]
print(split_by_first_char(sample))
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
# 41. Write a Python program to create multiple lists.
def create_multiple_lists(n):
    return [[] for _ in range(n)]

lists = create_multiple_lists(3)
print(lists)  # [[], [], []]
# 42. Write a Python program to find missing and additional values in two lists.
def compare_lists(list1, list2):
    missing = set(list1) - set(list2)
    additional = set(list2) - set(list1)
    return missing, additional

list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']
missing, additional = compare_lists(list1, list2)
print("Missing values in second list:", missing)
print("Additional values in second list:", additional)
# Missing: {'a', 'b', 'c'}
# Additional: {'g', 'h'}
# 43. Write a Python program to split a list into different variables.
data = [1, 2, 3]
a, b, c = data
print(a, b, c)  # 1 2 3
# 44. Write a Python program to generate groups of five consecutive numbers in a list.
def group_fives(n):
    return [list(range(i, i+5)) for i in range(1, n+1, 5)]

print(group_fives(20))
# [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
# 45. Write a Python program to convert a pair of values into a sorted unique array.
def pair_to_sorted_unique_array(pair):
    return sorted(set(pair))

print(pair_to_sorted_unique_array((5, 2)))
# [2, 5]
print(pair_to_sorted_unique_array((5, 5)))
# [5]
# 46. Write a Python program to select the odd items from a list.
def odd_items(lst):
    return lst[::2]  # chọn các phần tử ở vị trí lẻ (index 0,2,4,...)

print(odd_items([10, 20, 30, 40, 50]))
# [10, 30, 50]
# 47. Write a Python program to insert an element before each element of a list.
def insert_before_each(lst, element):
    result = []
    for item in lst:
        result.append(element)
        result.append(item)
    return result

print(insert_before_each([1, 2, 3], 0))
# [0, 1, 0, 2, 0, 3]
# 48. Write a Python program to print nested lists (each list on a new line) using the print() function.
def print_nested_lists(lst):
    for sublist in lst:
        print(sublist)

nested = [[1,2,3], [4,5,6], [7,8,9]]
print_nested_lists(nested)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# 49. Write a Python program to convert a list to a list of dictionaries.
def lists_to_dicts(names, codes):
    return [{"color_name": n, "color_code": c} for n, c in zip(names, codes)]

color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

print(lists_to_dicts(color_names, color_codes))
# [{'color_name': 'Black', 'color_code': '#000000'},
#  {'color_name': 'Red', 'color_code': '#FF0000'},
#  {'color_name': 'Maroon', 'color_code': '#800000'},
#  {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
# 50. Write a Python program to sort a list of nested dictionaries.
def sort_nested_dicts(lst, key):
    return sorted(lst, key=lambda x: x[key])

students = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 23}
]
print(sort_nested_dicts(students, "age"))
# [{'name': 'Alice', 'age': 22}, {'name': 'Bob', 'age': 23}, {'name': 'John', 'age': 25}]


