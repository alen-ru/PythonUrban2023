city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]


def num_cities_by_population(cities, max_population):
   filter_list_city = [dict_city["population"] for dict_city in cities if dict_city["population"] < max_population]
   num_cities = len(filter_list_city)
   return num_cities


max_population = 5  # Пороговое значение для населения

num_cities = num_cities_by_population(city_list, max_population)  # TODO найдите количество городов с населением меньшн 5 млн.

print(f"Количество городов с население до 5 млн. жителей равно = {num_cities}")
