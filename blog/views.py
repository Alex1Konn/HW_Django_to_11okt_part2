#Задание 5
# from django.shortcuts import render
# from itertools import groupby
#
# def index(request):
#     cities = [
#         "Амстердам",
#         "Берлин",
#         "Вена",
#         "Гамбург",
#         "Дублин",
#         "Екатеринбург",
#         "Женева",
#         "Загреб",
#         "Иркутск",
#         "Казань",
#         "Калининград",
#         "Лондон",
#         "Мадрид",
#         "Нижний Новгород",
#         "Новосибирск",
#         "Осло",
#         "Париж",
#         "Рим",
#         "Самара",
#         "Токио",
#         "Уфа",
#         "Флоренция",
#         "Хабаровск",
#         "Цюрих",
#         "Челябинск",
#         "Шанхай",
#         "Щёлково",
#         "Эдинбург",
#         "Южно-Сахалинск",
#         "Якутск",
#     ]
#
#     grouped_cities = []
#     for letter, group in groupby(cities, key=lambda x: x[0]):
#         grouped_cities.append({
#             'letter': letter,
#             'cities': list(group)
#         })
#
#     return render(request, 'blog/index.html', {'grouped_cities': grouped_cities})


# Задание 5
# from django.shortcuts import render
#
# def index(request):
#     students = [
#         {'first_name': 'Анна', 'last_name': 'Иванова'},
#         {'first_name': 'Борис', 'last_name': 'Петров'},
#         {'first_name': 'Виктория', 'last_name': 'Сидорова'},
#         {'first_name': 'Глеб', 'last_name': 'Кузнецов'},
#         {'first_name': 'Дарья', 'last_name': 'Морозова'},
#     ]
#
#     return render(request, 'blog/index.html', {'students': students})

# Задание 6
# from django.shortcuts import render
#
# def index(request):
#     tags = ['python', 'django', 'html']
#     return render(request, 'blog/index.html', {'tags': tags})


