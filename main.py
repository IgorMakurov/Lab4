#Написать программу, которая читая символы из файла, распознает, преобразует и выводит на экран объекты по определенному правилу.
#Объекты разделены пробелами. Распознавание и преобразование делать по возможности через регулярные выражения.
#Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.

#Вариант 13
#Целые числа, содержащие ровно 5 цифр. Вывести количество таких чисел. Минимальное число вывести прописью.

import re

digit_map = {
        '-': 'минус', '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }

five_digit_numbers = []


with open('input.txt', 'r') as file:
    content = file.read()
    matches = re.findall(r'-?\d{5}', content)
    five_digit_numbers = [int(match) for match in matches]

print("Найденные числа:")
for num in five_digit_numbers:
    print(num, end=" ")

count = len(five_digit_numbers)
print(f"\nКоличество чисел из 5 цифр: {count}")

if five_digit_numbers:
    min_number = min(five_digit_numbers)
    min_number_str = str(min_number)
    print("Минимальное число прописью:", end=" ")
    for digit in min_number_str:
        print(digit + ' ' + digit_map[digit], end=" ")
