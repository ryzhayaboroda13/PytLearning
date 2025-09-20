# -*- coding: utf-8 -*-
print("🎓 СИМУЛЯТОР ОБУЧЕНИЯ PYTHON")
print("---------------------------")

# Список тем, которые предстоит освоить
topics = ["Переменные", "Списки", "Условия if/else", "Циклы for", "Циклы while", "Функции"]
learned = []  # Сюда будем добавлять выученные темы

# Главный цикл обучения
while len(learned) < len(topics):
    current_topic = topics[len(learned)]    #задаем первый пункт обучения
    print(f"\n Тема для изучения №{len(learned) + 1}: {current_topic}")

    answer = input("Ты разобрался с темой? да/нет : ")

    if answer.lower() == 'да':
        learned.append(current_topic)
        print(f"✅ Отлично! '{current_topic}' — освоена!")
        print(f"Прогресс: {len(learned)}/{len(topics)} тем")
    else:
        print("❌ Нужно больше времени! Повтори материал еще раз.")

print("\n" + "="*50)
print("🎉 ТЫ ПОЛНОСТЬЮ ЗАКОНЧИЛ БАЗОВЫЙ КУРС PYTHON!")
print("Теперь ты готов к созданию Telegram-бота! 🚀")
print("="*50)