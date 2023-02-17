import requests
API_KEY = "8125ac9dc7fd2dcf2a828c333bbb931e" # API Key с сайта OpenWeatherMap
city_name = "Dolgoprudny" # Название города и код страны
country_code = "RU"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_KEY}" # Ссылка для запросов
response = requests.get(url) # Выполняем API запрос
data = response.json() # Парсинг данных JSON из ответа API
wind_speed = data["wind"]["speed"] # Извлечение скорости ветра и видимости из данных
visibility = data["visibility"]
print(f"Скорость ветра: {wind_speed} м/с") # Выводим скорость ветра и видимость
print(f"Видимость: {visibility} метров")