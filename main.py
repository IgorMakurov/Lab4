#Написать программу, которая читая символы из файла, распознает, преобразует и выводит на экран объекты по определенному правилу.
#Объекты разделены пробелами. Распознавание и преобразование делать по возможности через регулярные выражения.
#Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.

#Вариант 13
#Целые числа, содержащие ровно 5 цифр. Вывести количество таких чисел. Минимальное число вывести прописью.

import re

five_digit_numbers = []

with open('input.txt', 'r') as f:
    char = f.read()
    matches = re.findall(r'\b\d{5}\b', char)
    five_digit_numbers = [int(match) for match in matches]

count = len(five_digit_numbers)
print(f"Количество чисел из 5 цифр: {count}")

if five_digit_numbers:
    min_number = min(five_digit_numbers)
    min_number_str = str(min_number)
    print("Минимальное число прописью:", end=" ")
for digit in min_number_str:
    print(digit, end=" ")
