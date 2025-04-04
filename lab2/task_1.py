# import sys
#
# # #1.1
# num1 = float(sys.stdin.readline().strip())
# num2 = float(sys.stdin.readline().strip())
# num3 = float(sys.stdin.readline().strip())
#
# min_num = min(num1, num2, num3)
#
# print(f"Минимальное число: {min_num}")

# #1.2
# import sys
#
# num1 = float(sys.stdin.readline().strip())
# num2 = float(sys.stdin.readline().strip())
# num3 = float(sys.stdin.readline().strip())
#
# numbers = [num1, num2, num3]
# for num in numbers:
#     if 1 <= num <= 50:
#         print(f"Число {num} попадает в интервал [1, 50]")
#     else:
#         print(f"Число {num} не попадает в интервал [1, 50]")

# #1.3
# import sys
#
# m = float(sys.stdin.readline().strip())
#
# for i in range(1, 11):
#     print(f"{i} * {m} = {i * m}")


#1.4
import sys

input_data = sys.stdin.readline().strip()

numbers = []
current_number = ''
for char in input_data:
    if char == ' ':
        if current_number:
            numbers.append(int(current_number))
            current_number = ''
    else:
        current_number += char
if current_number:
    numbers.append(int(current_number))

sum_of_numbers = 0
count_of_numbers = 0

i = 0
while i < len(numbers):
    sum_of_numbers += numbers[i]
    count_of_numbers += 1
    i += 1

print(f"Сумма всех чисел: {sum_of_numbers}")
print(f"Количество всех чисел: {count_of_numbers}")
