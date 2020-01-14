import json

import calories


with open("Eda.json", "r") as read_file:
    food = json.load(read_file)
eats = calories.sum_cal(food)
print(eats['output'], 'Всего {} кКал'.format(eats['total']), sep='\n')
