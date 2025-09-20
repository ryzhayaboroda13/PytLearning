# -*- coding: utf-8 -*-
import random  # Импортируем модуль для случайного выбора

print("🎓 СИМУЛЯТОР ОБУЧЕНИЯ PYTHON")
print("---------------------------")

topics = ["Переменные", "Списки", "Условия if/else", "Циклы for", "Циклы while", "Функции"]
learned = []
attempts = {}  # Создаем словарь для подсчета попыток по каждой теме

# Создаем список мотивационных фраз
motivational_phrases = [
    "Так держать! Ты настоящий программист!",
    "Идеально! Движемся дальше!",
    "Превосходно! Следующая тема ждет!",
    "Ты уверенно идешь к своей цели!",
    "Еще один шаг к созданию Telegram-бота!"
]

# Задача 1: Выводим красивый список тем
print("Тебе предстоит освоить следующие темы:")
for i, topic in enumerate(topics, 1):
    print(f"  {i}. {topic}")
print("\n" + "="*40)

# Главный цикл обучения
while len(learned) < len(topics):
    current_index = len(learned)
    current_topic = topics[current_index]
    
    # Инициализируем счетчик попыток для темы, если его еще нет
    if current_topic not in attempts:
        attempts[current_topic] = 0
    attempts[current_topic] += 1  # Увеличиваем счетчик попыток
    
    print(f"\nТема для изучения #{current_index + 1}: {current_topic}")
    print(f"[Попытка #{attempts[current_topic]}]")
    
    answer = input("Ты разобрался с темой? (да/нет): ")
    
    if answer.lower() == 'да':
        learned.append(current_topic)
        # Задача 2: Выводим случайную мотивационную фразу
        random_phrase = random.choice(motivational_phrases)
        print(f"✅ {random_phrase}")
        print(f"Прогресс: {len(learned)}/{len(topics)} тем")
    else:
        print("🔄 Нужно больше времени! Повтори материал еще раз.")

# Финальная статистика
print("\n" + "="*50)
print("🎉 ТЫ ПОЛНОСТЬЮ ЗАКОНЧИЛ БАЗОВЫЙ КУРС PYTHON!")
print("\nСтатистика твоего обучения:")
for topic in topics:
    print(f"  {topic}: {attempts[topic]} попыток")
print("\nТеперь ты готов к созданию Telegram-бота! 🚀")
print("="*50)