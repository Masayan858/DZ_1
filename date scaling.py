#Скалировать полученное число в дату:

data = int(input())
if data <= 59: #цикл секунды
    print(data, 'сек') 
elif 60 <= data < 3600: #цикл минуты:
  minute = data // 60
  data = data % 60
  second = data
  print(minute, 'мин', second, 'сек')
elif 3600 <= data < 86400: #цикл часа:
  hour = data // 3600
  data = data % 3600
  minute = data // 60
  second = data % 60
  print(hour, 'час', minute, 'мин', second, 'сек')
elif 86400 <= data: #цикл дня:
  day = data // 86400
  data = data % 86400
  hour = data // 3600
  data = data % 3600
  minute = data // 60
  second = data % 60
  print(day, 'день', hour, 'час', minute, 'мин', second, 'сек')