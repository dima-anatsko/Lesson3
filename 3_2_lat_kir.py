def lat_kir(string):
    string = string.lower()
    lk = {
        'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'х',
        'i': 'и', 'j': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п',
        'q': 'к', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'v': 'в', 'w': 'в', 'x': 'х',
        'y': 'ы', 'z': 'з'
         }
    kl = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'jo', 'ж': 'zh', 'з': 'z',
        'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shh',
        'ъ': '#', 'ы': 'y', 'ь': '\'', 'э': 'je', 'ю': 'ju', 'я': 'ja'
         }
    if len(string) == 0:
        return ''
    if 97 <= ord(string[0]) <= 122:
        return ''.join(map(lambda x: (lk.get(x, x)), string))
    else:
        return ''.join(map(lambda x: (kl.get(x, x)), string))


s = input('Введите строку для транслитерации: ')
print(lat_kir(s))
