# -*- coding: utf-8 -*-
# 1. простые переменные
name = "Daniel"         #переменная типа str
age = 25                #переменная типа int
height = 1.85           #переменная типа float

# выводим на экране то что мы написали
print("Имя : ", name)
print("Возраст : ", age)
print("Рост : ", height)
print("----")

# 2. Длеаем операции с данными
year = int(input("Какой сейчас год?"))                      #компьютер уточняет какой сейчас год
print(name, "родился в :", year - age, "году")              #вычисляется год рождения и выводится результат

# 3. основные типы данных
#str    string      - строка,текст
message = "Это строка (str)"
#int    integer     - целое число
number_of_pets = 2
# float floating    - с запятой / дробное число
temperature = 36.6
# bool  boolean     - логические данные true/false
is_student = True

#print(message, number_of_pets, temperature, is_student)    #test

# 4. Функция type() gпоказывает тип данных в переменной

print("Тип переменной message:", type(message))
print("Тип переменной number_of_pets:", type(number_of_pets))
print("Тип переменной temperature:", type(temperature))
print("Тип переменной is_student:", type(is_student))

# 5. Динамическое изменение
# В одну и ту же коробку можно положить данные разных типов
x = 10
print("x - это число:", x)
x = "А теперь это строка"
print("x - теперь это:", x)