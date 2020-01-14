from copy import deepcopy


def mega_spis(sl, stop, spis, otv):
    perebor = set()
    for key, item in sl.items():
        if item in spis or item is None:
            perebor.add(key)
    for i in spis:
        if i in set(stop.keys()):
            perebor -= set(stop[i])
    if perebor:
        for i in perebor:
            b = deepcopy(spis)
            b.append(i)
            a = deepcopy(sl)
            del a[i]
            if not a:
                otv.append(b)
                return None
            else:
                mega_spis(a, stop, b, otv)
    else:
        otv.append(spis)
        return None


one = {1: 3, 2: None, 3: 2, 4: None}
two = {4: [2, 3]}
result = []
mega_spis(one, two, [], result)
print('Все возможные варианты:', result)
z = len(max(result, key=lambda x: len(x)))
print('Варианты с максимальной длиной:')
i = 1
for item in result:
    if len(item) == z:
        print('{}.)'.format(i), item)
        i += 1
