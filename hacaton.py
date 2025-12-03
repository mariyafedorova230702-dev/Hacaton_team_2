#1
# 1. Напишите функцию multiply(a, b)
# 2. Функция должна возвращать произведение двух чисел
# 3. Вызовите функцию с разными числами

# def multiply(a, b):
#     return a*b
# print(multiply(5,3))
# print(multiply(10,2))
# print(multiply(-5,4))

#2
# 1. Напишите функцию is_odd(n)
# 2. Возвращает True если число нечетное, False если четное
# 3. Вызовите для чисел: 3, 8, 11, 20

# def is_odd(n):
#     if n%2!=0:
#         return True
#     else:
#         return False
# print(is_odd(3))
# print(is_odd(8))
# print(is_odd(11))

#3
# 1. Напишите функцию count_consonants(text)
# 2. Подсчитайте количество согласных букв (все кроме а, е, и, о, у, я)
# 3. Используйте цикл for

# def count_consonants(text):
#     count=0
#     lst=[]
#     n='eyuioааэиоу' 
#     for i in text:
#         if i not in n:
#             count+=1
#             lst.append(i)
#     return count, lst
    
# print(count_consonants('hello'))
# print(count_consonants('Python'))
# print(count_consonants('аэиоу'))

#4
# 1. Напишите функцию is_anagram(text1, text2)
# 2. Проверяет являются ли два слова анаграммами
# 3. Анаграмма - слово из тех же букв в другом порядке

# def is_anagram(text1, text2):
#     for i in text1:
#         if i not in text2:
#             return False
#         else:
#             return True

# print(is_anagram('hello','world'))
# print(is_anagram('listen','silent'))
# print(is_anagram('abc','bca'))

#5
# 1. Напишите функцию min_three(a, b, c)
# 2. Возвращает самое маленькое число из трех
# 3. Не используйте встроенную функцию min()

# def min_three(a, b, c):
#     num=a
#     if num>b:
#         num=b
#     elif num>c:
#         num=c
#     return num
# print(min_three(5,10,3))
# print(min_three(100, 50, 75))
# print(min_three(1, 1, 1))




#Задача 6: Сумма элементов списка
# 1. Напишите функцию sum_list(numbers)
# 2. Принимает список чисел
# 3. Возвращает их сумму (используйте sum())
#
# Примеры:
# sum_list([1, 2, 3, 4, 5]) → 15
# sum_list([10, 20, 30]) → 60
# sum_list([100]) → 100

# def sum_list(numbers):
#     return sum(numbers)
# print(sum_list([1, 2, 3, 4, 5]))
# print(sum_list([10, 20, 30]))
# print(sum_list([100]))



#Задача 7: Реверс текста (разворот)
# 1. Напишите функцию reverse_text(text)
# 2. Разворачивает текст наоборот
# 3. Используйте slicing [::-1]
#
# Примеры:
# reverse_text("hello") → "olleh"
# reverse_text("Python") → "nohtyP"
# reverse_text("12345") → "54321
    
# def reverse_text(text):
#     return text[::-1]
# print(reverse_text("hello"))
# print(reverse_text("Python"))
# print(reverse_text("Python"))


#Задача 8: Перевод в нижний регистр
# 1. Напишите функцию to_lowercase(text)
# 2. Преобразует текст в нижний регистр
# 3. Используйте .lower()
#
# Примеры:
# to_lowercase("HELLO") → "hello"
# to_lowercase("PyThOn") → "python"
# to_lowercase("TEST") → "test"

# def to_lowercase(text):
#     return text.lower()
# print(to_lowercase("HELLO"))
# print(to_lowercase("PyThOn"))
# print(to_lowercase("TEST"))




#Задача 9: Фильтрация четных чисел
# 1. Напишите функцию filter_even(numbers)
# 2. Возвращает список только четных чисел
# 3. Используйте список comprehension или filter()
#
# Примеры:
# filter_even([1, 2, 3, 4, 5, 6]) → [2, 4, 6]
# filter_even([1, 3, 5]) → []
# filter_even([10, 20, 30]) → [10, 20, 30]


# def filter_even(numbers):
#     result = []
#     for n in numbers:
#         if n % 2 == 0:
#             result.append(n)
#     return result


# print(filter_even([1, 2, 3, 4, 5, 6]))
# print(filter_even([1, 3, 5]))
# print(filter_even([10, 20, 30]))


#Задача 10: Поиск максимального элемента
# 1. Напишите функцию find_max(numbers)
# 2. Находит максимальное число в списке
# 3. Не используйте встроенную функцию max()
#
# Примеры:
# find_max([3, 1, 4, 1, 5, 9]) → 9
# find_max([100, 50, 75]) → 100
# find_max([5]) → 5

# def find_max(numbers):
#     maximum = numbers[0]
#     for n in numbers:
#         if n > maximum:
#             maximum = n
#     return maximum        



# print(find_max([3, 1, 4, 1, 5, 9]))    
# print(find_max([100, 50, 75]))
# print(find_max([5]))



# def word_lengths(text):
#     """Подсчитывает длину каждого слова"""
#     leng = {'hello world': len('hello world')}
#     return leng
# print(word_lengths('hello world'))



# import time

# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()          
#         result = func(*args, **kwargs)
#         end = time.time()           
#         elapsed = end - start
#         print(f"Время выполнения: {elapsed:.2f} секунд")
#         return result
#     return wrapper


# @measure_time
# def slow_function():
#     time.sleep(2)
#     return "Done"
# print(slow_function())

# def uppercase_result(func):
#     def wrapper(text):
#         word = func(text)
#         return word.upper()
#     return wrapper


# @uppercase_result
# def message(text):
#     return text


# print(message("hello"))



# def multiply_all(*args):
#     a=list(args)
#     mlt=1
#     for i in a:
#         mlt*=i
#     return mlt
# print(multiply_all(2, 3, 4))
# print(multiply_all(5,10))
# print(multiply_all(1,1,1))
# print(multiply_all(2,3,4,5))

# def concat_strings(*args):
#     a=list(args)
#     words=' '.join(a)
#     return words
# print(concat_strings('Hello', 'World'))
# print(concat_strings('Python', 'is', 'awesome'))
# print(concat_strings('Test'))




