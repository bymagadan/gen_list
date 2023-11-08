list = [
    {'id': 1, 'full_name': 'Алекберов Рамиль Русланович'},
    {'id': 2, 'full_name': 'Бобровская Анастасия Дмитриевна'},
    {'id': 3, 'full_name': 'Винговатов Александр Олегович'}
]

student_list = [list['full_name'] for list in list]

for list in student_list:
    print(list)
