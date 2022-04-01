#склонение слова "процент" к числителю:
for j in range(1, 21):
    if j == 1:
        print(j, 'процент')
    elif 1 < j < 5:
        print(j, 'процента')
    else:
        print(j, 'процентов')
number = 21
while number <= 100:
    if number % 10 == 1:
        print(number, 'процент')
    elif number % 10 == 2:
        print(number, 'процента')
    elif number % 10 == 3:
        print(number, 'процента')
    elif number % 10 == 4:
        print(number, 'процента')
    else:
        print (number, 'процентов')
    number += 1