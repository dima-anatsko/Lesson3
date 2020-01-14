import json


def sum_cal(food):
    with open("./json/TableKallProd.json", "r") as read_file:
        data = json.load(read_file)
    result = {}
    total = 0
    for key in food:
        result[key] = int(data[key] * food[key] / 100)
        total += result[key]
    return {'input': food, 'output': result, 'total': total}
