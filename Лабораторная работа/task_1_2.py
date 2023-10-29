city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]

def average_population(cities):
    num_cities = len(cities)  # TODO найдите количество городов в списке
    list_population = [dict_city["population"] for dict_city in cities]
    total_population = sum(list_population)  # TODO найдите общее количество населения
    average = total_population / num_cities
    return average


average = average_population(city_list)
print(f"Среднее арифметическое населения равно = {average}")  # TODO распечатайте среднее арифметическое населения