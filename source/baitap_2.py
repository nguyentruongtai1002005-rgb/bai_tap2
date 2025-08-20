# 1. Write a Python program to calculate the length of a string
a = input("Nhập vào một chuỗi bất kỳ: ")
print (f"Độ dài của chuỗi là {len(a)}")
# 2. Write a Python program to count the number of characters (character frequency) in a string.
from collections import Counter
s = input("Nhập vào chuỗi: ")
freq = Counter(s)
print("Tần suất xuất hiện của các ký tự:")
print(dict(freq))
print("Tần suất xuất hiện của các ký tự:")
print(freq)
# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
a = input("Nhập vào một chuỗi bất kỳ: ")
b = len(a)
if b < 2:
    print ("Empty String!")
else:
    haikitudau = a[0:2]
    haikitucuoi = a[len(a)-2:len(a)]
    print (f"Kết quả lấy hai kí tự đầu và cuối ghép lại: {haikitudau + haikitucuoi}")
# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
a = input("Nhập vào một chuỗi bất kỳ: ")
b = a[0]                # lấy ký tự đầu tiên
c = a[1:].replace(b, '$')  # thay thế trong phần còn lại
result = b + c
print("Kết quả:", result)
# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
a = input("Nhập vào chuỗi thứ nhất: ")
b = input("Nhập vào chuỗi thứ hai: ")
c = a[0:2] + b[2:len(b)]
d = b[0:2] + a[2:len(a)]
print(f'Kết quả: {d + " " + c}')
# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
a = input("Nhập vào một chuỗi bất kỳ: ")
b = len(a) # Tìm độ dài của chuỗi
c = a[len(a)-3:len(a)] # Lấy ra 3 kí tự cuối của chuỗi
if b >= 3 and c!= "ing":
   a += "ing"
   print(f"Kết quả: {a}")
elif b<3:
   print(f"Kết quả: {a}")
else:
   print(f"Kết quả {a+"ly"}")
# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
s = input("Nhập vào chuỗi bất kỳ: ")
# Tìm vị trí của "not" và "poor"
not_index = s.find("not")
poor_index = s.find("poor")
# Nếu có cả "not" và "poor" và "not" đứng trước "poor"
if not_index != -1 and poor_index != -1 and not_index < poor_index:
    s = s[:not_index] + "good" + s[poor_index+4:]
# In kết quả
print("Kết quả:", s)
# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one
words_input = input("Nhập vào danh sách từ (cách nhau bằng khoảng trắng): ")
# Tách chuỗi thành list
words = words_input.split()
# Tìm từ dài nhất
longest_word = words[0]        # giả sử từ đầu tiên dài nhất
max_length = len(longest_word) # độ dài của từ đầu tiên
for word in words:
    word_length = len(word)   # độ dài của từ hiện tại
    if word_length > max_length:
        longest_word = word
        max_length = word_length
# In kết quả
print("Từ dài nhất: ", longest_word)
print("Số kí tự của từ dài nhất: ", max_length)
# 9. Write a Python program to remove the nth index character from a nonempty string.
# Nhập từ người dùng
chuoi = input("Nhập chuỗi: ")
n = int(input("Nhập vị trí index cần xóa: "))
def remove_char_at(s, n):
    # Kiểm tra n có hợp lệ không
    if n < 0 or n >= len(s):
        return "Index không hợp lệ!"
    # Ghép chuỗi bỏ qua ký tự tại vị trí n
    return s[:n] + s[n+1:]
# In kết quả
ket_qua = remove_char_at(chuoi, n)
print("Chuỗi sau khi xóa:", ket_qua)
# 10. Write a  Python program to change a given string to a newly string where the first and last chars have been exchanged.
# Nhập từ người dùng
chuoi = input("Nhập chuỗi: ")
# Nếu chuỗi dài <= 1 thì giữ nguyên
if len(chuoi) <= 1:
    ket_qua = chuoi
else:
    # Lấy ký tự đầu và ký tự cuối
    dau = chuoi[0]
    cuoi = chuoi[-1]
    # Phần ở giữa (bỏ đầu và cuối đi)
    giua = chuoi[1:-1]
    # Ghép lại: cuối + giữa + đầu
    ket_qua = cuoi + giua + dau
# In kết quả
print("Chuỗi sau khi hoán đổi:", ket_qua)
# 11. Write a Python program to remove characters that have odd index values in a given string
# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ")
# Giữ lại các ký tự có chỉ số chẵn
ket_qua = ""
for i in range(len(chuoi)):
    if i % 2 == 0:  # index chẵn
        ket_qua += chuoi[i]
print("Chuỗi sau khi xóa ký tự ở vị trí lẻ:", ket_qua)
# 12. Write a Python program to count the occurrences of each word in a given sentence.
# Nhập câu từ người dùng
cau = input("Nhập câu: ")
# Tách câu thành danh sách các từ
tu_list = cau.split()
# Dùng dictionary để đếm
dem = {}
for tu in tu_list:
    if tu in dem:
        dem[tu] += 1
    else:
        dem[tu] = 1
print("Số lần xuất hiện của mỗi từ:")
for tu, so_lan in dem.items():
    print(tu, ":", so_lan)
# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ")
print("Chữ hoa:", chuoi.upper())
print("Chữ thường:", chuoi.lower())
# 14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
# Nhập chuỗi từ người dùng
chuoi = input("Nhập các từ (ngăn cách bằng dấu phẩy): ")
# Tách các từ, bỏ khoảng trắng thừa
tu_list = [tu.strip() for tu in chuoi.split(",")]
# Lọc ra các từ khác nhau (set), rồi sắp xếp
tu_khac_nhau = sorted(set(tu_list))
# In kết quả
print("Kết quả:", ", ".join(tu_khac_nhau))
# 15. Write a  Python function to create an HTML string with tags around the word(s).
# Nhập từ người dùng
tag = input("Nhập tên thẻ HTML (vd: i, b, u...): ")   # Nhập tên thẻ
word = input("Nhập từ/câu cần bao quanh: ")           # Nhập từ/câu muốn gắn thẻ
# Hàm tạo chuỗi HTML với thẻ bao quanh
def add_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"
# In kết quả
print("👉 Kết quả:", add_tags(tag, word))
# 16. Write a Python function to insert a string in the middle of a string.
# Nhập từ người dùng
bracket = input("Nhập chuỗi khung (vd: [[]], {{}}): ")   # Nhập chuỗi khung
word = input("Nhập chuỗi muốn chèn vào giữa: ")          # Nhập chuỗi cần chèn
# Hàm chèn chuỗi word vào giữa chuỗi bracket
def insert_string_middle(bracket, word):
    mid = len(bracket) // 2   # Tính vị trí giữa
    return bracket[:mid] + word + bracket[mid:]  # Ghép lại: phần đầu + word + phần sau
# In kết quả
print("Kết quả:", insert_string_middle(bracket, word))
# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# Nhập từ người dùng
chuoi = input("Nhập chuỗi (ít nhất 2 ký tự): ")   # Nhập chuỗi
# Hàm tạo chuỗi gồm 4 bản sao của 2 ký tự cuối
def insert_end(s):
    if len(s) < 2:    # Nếu chuỗi quá ngắn thì báo lỗi
        return "Chuỗi phải dài ít nhất 2 ký tự"
    last2 = s[-2:]    # Lấy 2 ký tự cuối
    return last2 * 4  # Lặp lại 4 lần
# In kết quả
print("Kết quả:", insert_end(chuoi))
# 18. Write a  Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
# Nhập từ người dùng
chuoi = input("Nhập chuỗi: ")   # Nhập chuỗi
# Hàm lấy 3 ký tự đầu tiên
def first_three(s):
    if len(s) < 3:    # Nếu chuỗi ngắn hơn 3 ký tự
        return s      # Trả nguyên chuỗi
    return s[:3]      # Ngược lại, lấy 3 ký tự đầu
# In kết quả
print("Kết quả:", first_three(chuoi))
# 19. Write a Python program to get the last part of a string before a specified characte
# Nhập từ người dùng
chuoi = input("Nhập chuỗi (vd: đường link): ")   # Nhập chuỗi
ky_tu = input("Nhập ký tự cần cắt trước (mặc định là '/'): ")   # Nhập ký tự cần cắt
# Nếu không nhập ký tự thì mặc định là "/"
if ky_tu.strip() == "":
    ky_tu = "/"
# Hàm cắt chuỗi: lấy phần trước ký tự cuối cùng xuất hiện
def get_last_part(s, char="/"):
    return s.rsplit(char, 1)[0]   # rsplit tách từ bên phải, số lần = 1
# In kết quả
print("Kết quả:", get_last_part(chuoi, ky_tu))
# 20. Write a  Python function to reverse a string if its length is a multiple of 4.
# Nhập từ người dùng
chuoi = input("Nhập chuỗi: ")
def reverse_if_multiple_of_4(s):
    if len(s) % 4 == 0:   # Kiểm tra độ dài có chia hết cho 4 không
        return s[::-1]    # Đảo chuỗi
    return s              # Nếu không thì giữ nguyên
print("Kết quả:", reverse_if_multiple_of_4(chuoi))
# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2  uppercase characters in the first 4 characters.
# Nhập từ người dùng
chuoi = input("Nhập chuỗi: ")
def to_upper_if_condition(s):
    # Đếm số chữ hoa trong 4 ký tự đầu
    count_upper = sum(1 for c in s[:4] if c.isupper())
    if count_upper >= 2:
        return s.upper()
    return s
print("Kết quả:", to_upper_if_condition(chuoi))
# 22.Write a  Python program to sort a string lexicographically.
# Nhập từ người dùng
chuoi = input("Nhập chuỗi: ")
# Sắp xếp ký tự theo alphabet
ket_qua = "".join(sorted(chuoi))
print("Kết quả:", ket_qua)
# 23. Write a Python program to remove a newline in Python.
# Nhập từ người dùng
print("Nhập chuỗi (có thể gõ nhiều dòng, bấm Enter rồi Ctrl+D / Ctrl+Z để kết thúc):")
import sys
chuoi = sys.stdin.read()   # Đọc nhiều dòng từ input
# Xóa ký tự xuống dòng
ket_qua = chuoi.replace("\n", "")
print("Kết quả:", ket_qua)
# 24. Write a Python program to check whether a string starts with specified characters.
# Nhập từ người dùng
chuoi = input("Nhập chuỗi: ")
prefix = input("Nhập ký tự/chuỗi cần kiểm tra: ")
if chuoi.startswith(prefix):
    print("Chuỗi bắt đầu bằng:", prefix)
else:
    print("Chuỗi KHÔNG bắt đầu bằng:", prefix)
# 25. Write a Python program to create a Caesar encryption.
# Nhập từ người dùng
text = input("Nhập chuỗi cần mã hóa: ")
shift = int(input("Nhập số bước dịch (vd: 3): "))
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():   # Nếu là chữ cái
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char   # Giữ nguyên nếu không phải chữ cái
    return result
print("Chuỗi mã hóa:", caesar_encrypt(text, shift))
# 26. Write a  Python program to display formatted text (width=50) as output.
import textwrap
chuoi = input("Nhập chuỗi: ")
print(textwrap.fill(chuoi, width=50))
# 27. Write a  Python program to remove existing indentation from all of the lines in a given text.
import textwrap
chuoi = """    Đây là dòng có thụt vào
        Đây cũng vậy
    Lại thêm dòng nữa"""
print(textwrap.dedent(chuoi))
# 28. Write a Python program to add prefix text to all of the lines in a string.
chuoi = """Dòng 1
Dòng 2
Dòng 3"""
prefix = input("Nhập prefix: ")
print("\n".join(prefix + line for line in chuoi.splitlines()))
# 29. Write a Python program to set the indentation of the first line.
chuoi = input("Nhập chuỗi: ")
indented = "    " + chuoi
print(indented)
# 30. Write a Python program to print the following numbers up to 2 decimal places.
num = float(input("Nhập số: "))
print("Kết quả: {:.2f}".format(num))
# 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.
num = float(input("Nhập số: "))
print("Kết quả: {:+.2f}".format(num))
# 32. Write a Python program to print the following positive and negative numbers with no decimal places.
so_duong = float(input("Nhập số dương: "))
so_am = float(input("Nhập số âm: "))
print("Kết quả:", "{:.0f}".format(so_duong), "{:.0f}".format(so_am))
# 33. Write a  Python program to print the following integers with zeros to the left of the specified width.
num = int(input("Nhập số: "))
width = int(input("Nhập chiều rộng: "))
print("Kết quả:", str(num).zfill(width))
# 34. Write a  Python program to print the following integers with '*' to the right of the specified width.
num = int(input("Nhập số: "))
width = int(input("Nhập chiều rộng: "))
print("Kết quả:", f"{num:*<{width}}")
# 35. Write a Python program to display a number with a comma separator.
num = int(input("Nhập số: "))
print("Kết quả:", "{:,}".format(num))
# 36. Write a Python program to format a number with a percentage.
num = float(input("Nhập số: "))
print("Kết quả:", "{:.2%}".format(num))
# 37. Write a Python program to display a number in left, right, and center aligned with a width of 10.
num = input("Nhập số: ")
print("Trái:", "{:<10}".format(num))
print("Phải:", "{:>10}".format(num))
print("Giữa:", "{:^10}".format(num))
# 38. Write a Python program to count occurrences of a substring in a string.
chuoi = input("Nhập chuỗi: ")
sub = input("Nhập chuỗi con: ")
print("Số lần xuất hiện:", chuoi.count(sub))
# 39. Write a  Python program to reverse a string.
chuoi = input("Nhập chuỗi: ")
print("Chuỗi đảo ngược:", chuoi[::-1])
# 40. Write a Python program to reverse words in a string.
chuoi = input("Nhập chuỗi: ")
print("Đảo từ:", " ".join(chuoi.split()[::-1]))
# 51. Write a  Python program to find the first non-repeating character in a given string.
chuoi = input("Nhập chuỗi: ")  # Nhập chuỗi từ người dùng
for ch in chuoi:  # Duyệt từng ký tự
    if chuoi.count(ch) == 1:  # Nếu ký tự chỉ xuất hiện 1 lần
        print("Ký tự không lặp đầu tiên:", ch)
        break
else:  # Nếu không tìm thấy
    print("Không có ký tự nào duy nhất")
# 52. Write a Python program to print all permutations with a given repetition number of characters of a given string.
import itertools
chuoi = input("Nhập chuỗi: ")
n = int(input("Nhập độ dài hoán vị: "))
# itertools.product tạo ra hoán vị có lặp
perms = itertools.product(chuoi, repeat=n)
for p in perms:
    print("".join(p))  # Ghép tuple thành chuỗi
# 53. Write a Python program to find the first repeated character in a given string.
chuoi = input("Nhập chuỗi: ")
seen = set()  # Tập hợp để lưu ký tự đã gặp
for ch in chuoi:
    if ch in seen:  # Nếu gặp lại ký tự
        print("Ký tự lặp đầu tiên:", ch)
        break
    seen.add(ch)  # Thêm ký tự vào tập
else:
    print("Không có ký tự lặp")
# 54. Write a  Python program to find the first repeated character in a given string where the index of the first occurrence is smallest.
chuoi = input("Nhập chuỗi: ")
for i, ch in enumerate(chuoi):  # Duyệt từng ký tự với index
    if chuoi.count(ch) > 1:  # Nếu ký tự xuất hiện nhiều hơn 1 lần
        print("Ký tự lặp đầu tiên (index nhỏ nhất):", ch)
        break
# 55. Write a Python program to find the first repeated word in a given string.
chuoi = input("Nhập chuỗi: ")
words = chuoi.split()  # Tách thành list từ
seen = set()
for w in words:
    if w in seen:  # Nếu gặp lại từ
        print("Từ lặp đầu tiên:", w)
        break
    seen.add(w)
else:
    print("Không có từ lặp")
# 56. Write a Python program to find the second most repeated word in a given string.
from collections import Counter
chuoi = input("Nhập chuỗi: ")
words = chuoi.split()
counts = Counter(words).most_common()  # Đếm số lần xuất hiện
if len(counts) >= 2:
    print("Từ lặp nhiều thứ 2:", counts[1][0])
else:
    print("Không đủ từ để tìm")
# 57. Write a  Python program to remove spaces from a given string.
chuoi = input("Nhập chuỗi: ")
# Thay thế toàn bộ khoảng trắng bằng chuỗi rỗng
print("Kết quả:", chuoi.replace(" ", ""))
# 58. Write a Python program to move spaces to the front of a given string.
chuoi = input("Nhập chuỗi: ")
spaces = chuoi.count(" ")  # Đếm số lượng khoảng trắng
no_space = chuoi.replace(" ", "")  # Xóa khoảng trắng
print("Kết quả:", " " * spaces + no_space)  # Đưa khoảng trắng lên đầu
# 59. Write a Python program to find the maximum number of characters in a given string.
from collections import Counter
chuoi = input("Nhập chuỗi: ")
counts = Counter(chuoi)  # Đếm tần suất từng ký tự
max_char = max(counts, key=counts.get)  # Lấy ký tự có số lần xuất hiện lớn nhất
print("Ký tự xuất hiện nhiều nhất:", max_char, "(", counts[max_char], "lần )")
# 60. Write a  Python program to capitalize the first and last letters of each word in a given string.
chuoi = input("Nhập chuỗi: ")
result = []
for word in chuoi.split():
    if len(word) == 1:  # Nếu từ chỉ có 1 ký tự
        result.append(word.upper())
    else:
        # Viết hoa chữ đầu và cuối
        result.append(word[0].upper() + word[1:-1] + word[-1].upper())
print(" ".join(result))  # Ghép lại thành chuỗi
