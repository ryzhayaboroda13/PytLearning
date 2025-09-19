# Это наш список проектов. Можешь менять его как хочешь!
my_projects = []
#count = 0
while True:     #infinite loop
    user_input_project = input("Перечисли проекты которыми ты хочешь заняться (остановить -> стоп): ")
    if user_input_project.lower() == "стоп":
        print(f"Ты указал следущее количество проектов {len(my_projects)}")
        longest_project_name = ""       #поиск самого длинного названия проекта
        #  моя изначальная версия до корректировки от ии
        # for project in my_projects:
        #     count += 1
        #     if len(project) > len(longest_project_name):
        #         longest_project_name = project 
        for index, project in enumerate(my_projects, 1):
            print(f"Проект #{index}->", project)  
            if len(project) > len(longest_project_name):
                longest_project_name = project 
        print(f"Проект с самым длинным названием: '{longest_project_name}'")
        print("---")      
        break
    else:
         my_projects.append(user_input_project)
         print(f"Отлично! Ты добавил ещё: '{user_input_project}'.")
        


