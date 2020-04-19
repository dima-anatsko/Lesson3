# Lesson3
#tasks Пожалуйста выполняйте каждое из заданий в отдельном файле.

Дается словарь с ключами и значениями формата int. Вернуть новый словарь, в котором ключам по возрастанию будут присвоены значения по возрастанию. Пример: {1: 5, 4: 3, 2: 2} -> {1: 2, 2: 3, 4: 5}. Формат: dict -> dict

Написать скрипт, который будет получать на входе кириллическую строку и переводить её в латиницу. «Привет мир» -> «Privet mir» Реализовать логику обратной операции латиница -> кириллица. Определять попала на ввод кириллица или латиница по первой букве входящей строки. Учитывать регистр букв для вывода не обязательно.

Дается два списка с цифрами. Вернуть 1) список с цифрами, которые есть в обоих входящих списках; 2) список с цифрами, которые естьв первом списке и нет во втором; 3) список с цифрами, которые уникальны для каждого из двух входящих списков(нет в обоих входящих списках). Сторонними модулями не пользоватся.

Дается два списка с цифрами. Объединить их в один список. Удалить дубликаты элементов. Отсортировать по убыванию и вывести результат.

Дается строка символов. Найти все уникальные символы в строке и посчитать сколько раз они в нем встречаются. Вывести результат в виде словаря {символ: кол-во встреч}

Дается tuple(кортеж) имен. Нужно перебрать его и вывести фразу типа «Привет [имя]!»

Дается tuple(кортеж) каждый элемент которого является кортежем с именем и номеров кабинета. Пр. ((‘Виталий’, 243), (‘Виктор’, 404)….) Нужно перебрать его и вывести фразу типа «[имя] пройдите пожалуйста в кабинет номер [номер кабинета]»

Написать программу расчета суточного потребления калорий. В программе должен быть словарь, ключами которого являются названия продуктов, а значения – калорийностью на 100г, пр. {‘гречка’: 110, ‘вода’: 0; ‘молоко3.2’: 58}. На вход программа получает словарь типа {‘продукт’: количество потребленных грамм}(запишите словарь в коде, т.к. вручную с клавиатуры вести его затруднительно)

Программа на выход должна выдавать словарь {‘продукт’: количество потребленных калорий}. А так же суммарное количество потребленных калорий.

Кто хочет задачки сложнее(по желанию):

8.1) Сделайте загрузку словаря с калорийностью и входные данные из файла в формате JSON 8.2) Сделайте загрузку словаря с калорийностью из файла в формате JSON, а саму программу в виде веб сервера принимающего POST запрос с входными данными в виде JSON и отдающего ответ в так же в JSON формате. Для веб сервера возьмите webpy.org или palletsprojects.com/p/flask, для написания запросов к серверу getpostman.com

Нужно выстроить список элементов в такой последовательности, чтобы в него вошло максимально большое количество элементов. Дано два словаря. Первый словарь – {элемент: необходимый для него элемент}. Пр. {1: 3, 2: None, 3: 2, 4: None}. Условие 1: элемент можно включить в список если у него нет необходимого элемента, или необходимый элемент был добавлен в список. Из примера выше решением будет [2, 3, 4, 1] или [4, 2, 3, 1]. Неправильно: [1, 2…] т.к. 1 элемент может быть добавлен только после 3. Второй словарь – {элемент: список блокируемых элементов}. Т.е. после добавления этого элемента нельзя добавить элементы из списка. Пр. {4: [2, 3]} – в таком случае решением будет только [2, 3, 4, 1]. Неправильно [4, 2, 3, 1] – т.к. после 4 мы не может добавить 2 и 3.
