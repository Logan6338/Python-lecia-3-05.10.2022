## lambda функции

# def f(x):
#     return x**2
# g = f
# print(type(f))
# print(type(g))
# print(f(4))
# print(f(4))


# def calc(x):
#     return x+10
# ##print(calc(10))
# def calc2(x):
#     return x*10
# ##print(calc2(10))

# def math(op, x):
#     print(op(x))
# math(calc2, 10)
# math(calc, 10)



# list = []
# for i in range(1, 101):
#     if (i % 2 == 0):
#         list.append(i)
# print(list)

## Тоже самое только записано одной строчкой

# list = [i for i in range(1,21) if i % 2 == 0]
# print(list)

## Вывести список картежей

# list = [(i, i) for i in range(1,21) if i % 2 == 0]
# print(list)


## С функцией

# def f(x):
#     return x**3
# list = [f(i) for i in range(1,21) if i % 2 == 0]
# print(list)

## Функция с картежем (будет показано число и функция возведения в степень)
# def f(x):
#     return x**3
# list = [(i, f(i)) for i in range(1,21) if i % 2 == 0]
# print(list)

### Задача 
# # В файле хранятся числа, нужно выбрать четные и
# # составить список пар (число; квадрат числа).
# # Пример:
# # 1 2 3 5 8 15 23 38
# # Получить:
# # [(2, 4), (8, 64), (38, 1444)]

# list = [1, 2, 3, 5, 8, 15, 23, 38]
# def f(x):
#     return x**2
# list = [(i, f(i)) for i in list if i % 2 == 0]
# print(list) # Задача решена без отдельного файла!!!!!

### Полное решение преподавателя с использованием файла!!!!

# path = 'C:/Users/Logan/Desktop/GeekBrains/Знакомство с языком Python/3 урок/Python lecia 3 06.10.2022/file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)

### Улучшение кода задачи

# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return[x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x:(x, x**2), res)
# print(res)

#### Функция MAP

# li = [x for x in range(1, 20)]
# li = list(map(lambda x:x+10, li))
# print(li)

### Решение предыдушей задачи через MAP
# 1 2 3 45 67

data =list(map(int, input().split()))
print(data) 