import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 45.0448,  # широта Краснодара
    "longitude": 38.976,  # долгота Краснодара
    "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum,sunrise,sunset,daylight_duration",
    "timezone": "Europe/Moscow"
}
response = requests.get(BASE_URL, params=params)
if response.status_code == 200:
    data = response.json()
    tomorrow_temp_min = data['daily']['temperature_2m_min'][1]
    tomorrow_temp_max = data['daily']['temperature_2m_max'][1]
    tomorrow_precipitation = data['daily']['precipitation_sum'][1]
    tomorrow_sunrise = data['daily']['sunrise'][1]
    tomorrow_sunset = data['daily']['sunset'][1]
    tomorrow_daylight_duration = int(data['daily']['daylight_duration'][1]/3600)

    print(f"Прогноз погоды в Краснодаре на завтра:")
    print(f"Минимальная температура: {tomorrow_temp_min}°C")
    print(f"Максимальная температура: {tomorrow_temp_max}°C")
    print(f"Ожидаемое количество осадков: {tomorrow_precipitation} мм")
    print(f"Время восхода солнца: {tomorrow_sunrise}")
    print(f"Время захода солнца: {tomorrow_sunset}")
    print(f"Продолжительность дня: {tomorrow_daylight_duration} часов")
else:
    print(f"Ошибка {response.status_code}: {response.text}")

from PIL import Image
filename = 'buildings.jpg'
with Image.open(filename, 'r') as img:
    img.load()
    img.show()
    print(img.size)
    cropped_img = img.crop((640,170, 860, 960))
    print(cropped_img.size)
    cropped_img.show()
    low_res_img = cropped_img.reduce(2)
    print(low_res_img.size)
    low_res_img.show()
    cropped_img.save('cropped_img.jpg')
    low_res_img.save('low_res_img.png')
    img_1 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img_1.show()
    img_2 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img_2.show()
    rotate_img = img.rotate(45)
    rotate_img.show()
    rotate_img = img.rotate(32,expand=True)
    rotate_img.show()

filename_1 = 'strawberry.jpg'
with Image.open(filename_1, 'r') as img_1:
    img_1.load()
    img_1.show()
    cmyk_img = img_1.convert("CMYK")
    cmyk_img.show()
    gray_img = img_1.convert("L")
    gray_img.show()
    gray_img.save('gray_img.png')
