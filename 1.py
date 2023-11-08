name = [
{'id':1, 'full_name': 'Алекберов Рамиль Русланович'},
{'id':2, 'full_name': 'Бобровская Анастасия Дмитриевна'},
{'id':2, 'full_name': 'Винговатов Александр Олегович'},

]

f_name = [name['full_name'] for name in name if len(name['full_name'].split()[1]) > 6]

print (f_name)
