import requests
city = 'Moscow, RU'
appid = 'c2c631b10600b9dfbfed840b85121be8'
res = requests.get("http://api.openweathermap.org/data/2.5/weather",\
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data=res.json()
print('Прогноз погоды на сегодня:')
print('Город:', city)
print('Погодные условия:', data['weather'][0]['description'])
print('Температура:', data['main']['temp'])
print('Минимальная температура:', data['main']['temp_min'])
print('Максимальная температура', data['main']['temp_max'])
print('Скорость ветра:',data['wind']['speed'], 'м\с')
print('Видимость',data['visibility'], 'м')
print()
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",\
                   params={'q': city,'units':'metric','lang':'ru','APPID': appid})
data = res.json()
print('Прогноз погоды на неделю:')
for i in data['list']:
    print("Дата <", i['dt_txt'],"> \r\nТемпература<",'{0:+3.0f}'\
          .format(i['main']['temp']),"> \r\nПогодныеусловия <",\
          i['weather'][0]['description'],">", "> \r\nСкорость ветра <",\
          i['wind']['speed'], "> \r\nВидимость <", i['visibility'], ">")
    print("____________________________")