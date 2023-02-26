import requests
import pprint
import time

DOMAIN = 'https://api.hh.ru/'

url_vacancies = f'{DOMAIN}vacancies'

params = {
    'text': 'python developer',
    'page': 1
}

result = requests.get(url_vacancies, params=params).json()

# pprint.pprint(result.json())

# 1. количество найденных вакансий
vacancies = result['found']
items = result['items']
print(vacancies)

# выявляем ключевые скиллы в вакансиях на стр.1
# после получения списка выписываем скиллы и комментим код

# for item in items:
#     url = item['url']
#     result = requests.get(url).json()
#     print(result['key_skills'])
#     time.sleep(1)

# добавляем зарплату в лист
salary_list = []
for a, b in result.items():
    if isinstance(b, list):
        for c in b:
            for d, e in c.items():
                if isinstance(e, dict):
                    if d == 'salary':
                        for f, g in e.items():
                            if f == 'from' and e['currency'] == 'RUR' and isinstance(g, int):
                                salary_list.append(g)
                            else:
                                pass
my_sum = 0
for i in salary_list:
    my_sum += i


# my_sum - средняя зарплата
my_sum = my_sum / len(salary_list)


# словарь с ключевыми навыками
requirements = {'Python': 0, 'Django Framework': 0, 'Git': 0, 'PostgreSQL': 0, 'numpy': 0, 'MySql': 0, 'MongoDB': 0, 'Docker': 0}


# считаем требования в вакансиях
for a, b in result.items():
    if isinstance(b, list):
        for c in b:
            for d, e in c.items():
                if isinstance(e, dict):
                    if d == 'snippet':
                        for f, g in e.items():
                            if f == 'requirement':
                                for h, j in requirements.items():
                                    if h in g:
                                        requirements[h] += 1
                            else:
                                pass


# сохраняем данные в файл
f = open('Данные по вакансиям', 'w')

f.write(f'Данные по вакансиям:\nНайдено вакансий: {vacancies}\n'
        f'Требования в вакансиях с первой страницы hh: {requirements}\n'
        f'Средняя зп на первой странице: {my_sum}')

f.close()