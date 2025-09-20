# Объявляем функцию для проверки, является ли слово палиндромом
# (читается одинаково слева направо и справа налево)


def is_palindrome(word):
    # Приводим слово к нижнему регистру для регистронезависимой проверки
    word = word.lower()
    # Сравниваем слово с его перевернутой версией
    return word == word[::-1]


# Объявляем функцию для подсчета символов в тексте
def count_characters(text):
    # Удаляем все пробелы из текста
    text_without_spaces = text.replace(" ", "")
    # Возвращаем длину полученной строки
    return len(text_without_spaces)


# Объявляем функцию для создания никнейма
def create_nickname(name):
    # Генерируем случайное число от 1 до 999
    import random
    number = random.randint(1, 999)
    # Создаем никнейм: Super + Имя + Число
    return f"Super{name}{number}"


# === ОСНОВНАЯ ПРОГРАММА ===
print("=== МИНИ-УТИЛИТЫ ДЛЯ РАБОТЫ С ТЕКСТОМ ===")
print()

# Демонстрация работы функции is_palindrome
print("1. Проверка палиндромов:")
test_words = ["казак", "машина", "Anna", "топот"]
for word in test_words:
    # Вызываем функцию для каждого слова и сохраняем результат
    result = is_palindrome(word)
    print(f"   '{word}' -> {'палиндром' if result else 'не палиндром'}")
print()

# Демонстрация работы функции count_characters
print("2. Подсчет символов (без пробелов):")
test_text = "Hello World Python"
# Вызываем функцию и передаем ей текст
char_count = count_characters(test_text)
print(f"   Текст: '{test_text}'")
print(f"   Символов без пробелов: {char_count}")
print()

# Демонстрация работы функции create_nickname
print("3. Генерация никнейма:")
# Вызываем функцию с твоим именем
nickname = create_nickname("Daniel")
print(f"   Твой новый никнейм: {nickname}")
print()

# Показываем, как функции можно комбинировать
print("4. Комбинирование функций:")
phrase = "А роза упала на лапу Азора"
# Используем результат одной функции как аргумент для другой
print(f"   Фраза: '{phrase}'")
print(f"   Это палиндром: {is_palindrome(phrase)}")
print(f"   Символов без пробелов: {count_characters(phrase)}")