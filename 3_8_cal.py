data = {'вино': 171, 'водка': 235, 'пиво': 42, 'молоко3.2': 58, 'вода': 0,
        'гречка': 110, 'манка': 98, 'овсянка': 102, 'рис': 97, 'хлеб': 208}
eda = {'пиво': 2000, 'молоко3.2': 500, 'вода': 1000, 'хлеб': 150}
result = {}
total = 0
for key in eda:
    result[key] = int(data[key] * eda[key] / 100)
    total += result[key]
print(result, 'Всего калорий: {}'.format(total), sep='\n')
