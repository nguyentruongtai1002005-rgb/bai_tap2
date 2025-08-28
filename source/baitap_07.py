# Bài 1
# 1.Write python program:
# a) Convert two lists into a dictionary
keys = ["name", "age", "city"]
values = ["Tai", 20, "Ho Chi Minh City"]
dict_a = dict(zip(keys, values))
print("a) Dictionary:", dict_a)

# b) Merge two Python dictionaries into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("b) Merged:", merged_dict)

# c) Print the value of key ‘history’
sample_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {"math": 85, "history": 80}
        }
    }
}
print("c) History:", sample_dict["class"]["student"]["marks"]["history"])

# d) Initialize dictionary with default values
employees = ["Tuan", "Hoa", "Lan"]
default_value = 1000
dict_d = dict.fromkeys(employees, default_value)
print("d) Initialized:", dict_d)

# e) Create dictionary by extracting keys from a given dictionary
original_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_extract = ["a", "c"]
dict_e = {k: original_dict[k] for k in keys_extract}
print("e) Extracted:", dict_e)

# f) Delete a list of keys from a dictionary
dict_f = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_delete = ["b", "d"]
for k in keys_delete:
    dict_f.pop(k, None)
print("f) After delete:", dict_f)

# g) Check if a value exists in a dictionary
dict_g = {"x": 10, "y": 20, "z": 30}
value_check = 20
print("g) Exists?", value_check in dict_g.values())

# h) Rename key of a dictionary
dict_h = {"name": "Tai", "age": 20}
dict_h["fullname"] = dict_h.pop("name")
print("h) Renamed:", dict_h)

# i) Get the key of a minimum value
dict_i = {"a": 5, "b": 2, "c": 7}
min_key = min(dict_i, key=dict_i.get)
print("i) Min key:", min_key)

# j) Change value of a key in a nested dictionary
dict_j = {"emp": {"name": "Tai", "age": 20}}
dict_j["emp"]["age"] = 25
print("j) Updated:", dict_j)

# 2.Write a Python program that counts the number of times characters appear in a text paragraph.
text = "Python is fun and Python is powerful"
char_count = {}

for ch in text:
    if ch != " ":  # bỏ qua khoảng trắng
        char_count[ch] = char_count.get(ch, 0) + 1

print("2) Character count:", char_count)
# 3. Write a program using a dictionary containing keys starting from 1 and values​​containing prime numbers less than a value N.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_dict(N):
    primes = [x for x in range(N) if is_prime(x)]
    return {i+1: primes[i] for i in range(len(primes))}

N = 20
print("3) Prime dict:", prime_dict(N))
# Bài 2: Restructuring the company data: Suppose you have a dictionary that contains information about employees at a company. Each employee is identified by an ID number, and their information includes their name, department, and salary. You want to create a nested dictionary that groups employees by department so that you can easily see the names and salaries of all employees in each department. Write a Python program that when given a dictionary, employees, outputs a nested dictionary, dept_employees, which groups employees by department.
employees = {
    1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
    1002: {"name": "Bob", "department": "Sales", "salary": 50000},
    1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
    1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
    1005: {"name": "Eve", "department": "Sales", "salary": 55000}
}

dept_employees = {}

for emp_id, info in employees.items():
    dept = info["department"]
    if dept not in dept_employees:
        dept_employees[dept] = {}
    # copy thông tin nhưng bỏ field "department"
    dept_employees[dept][emp_id] = {
        "name": info["name"],
        "salary": info["salary"]
    }

print(dept_employees)
