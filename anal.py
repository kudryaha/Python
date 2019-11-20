def money_reader(what, where, when):
    """
    Функция возвращает некоторый показатель по сведениям Сбербанка в выбранном городе за указанный период.
    what - что ищем, например 'Средняя зарплата'.
    where - где ищем, например 'Санкт-Петербург'.
    when - когда ищем, указываем год. print('max: ', max(money), 'month: ', row[2])
    """
    import csv
    money = list()
    try:
        with open('opendata.csv', encoding='cp1251') as csvfile:
            money_reader = csv.reader(csvfile) # delimiter по умолчанию ','
            for row in money_reader:
                if row[0] == what:
                    if row[1] == where:
                        lst = row[2].split('-')
                        if lst[0] == when:
                            money.append(int(row[3]))
        return round(sum(money)/len(money), 2)
    except Exception as e:
        return e

def max_money(what, where, when1, when2):
    import csv
    money = list()
    maxx = -1
    try:
        with open('opendata.csv', encoding='cp1251') as csvfile:
            money_reader = csv.reader(csvfile) # delimiter по умолчанию ','
            for row in money_reader:
                if row[0] == what:
                    if row[1] == where:
                        lst = row[2].split('-')
                        if when1 < int(lst[0]) <= when2:
                            money.append(int(row[3]))
                        if int(row[3]) > maxx:
                            maxx = int(row[3])
                            month = row[2].split('-')[1]
        return max(money), month
    except Exception as e:
        return e

def region(what):
    import csv
    zaya = {}
    try:
        with open('opendata.csv', encoding='cp1251') as csvfile:
            money_reader = csv.reader(csvfile) # delimiter по умолчанию ','
            for row in money_reader:
                if row[0] == what:
                    if row[1] not in zaya.keys() and row[1] != 'Россия':
                        zaya[row[1]] = int(row[3])
                    if row[1] in zaya.keys():
                        zaya[row[1]] += int(row[3])
        return max(zaya.items(), key=lambda k: k[1])
    except Exception as e:
        return e


if __name__ == '__main__':

    print('Санкт-Петербург')
    for year in range(2015, 2019):
        print(str(year), money_reader('Средняя зарплата', 'Санкт-Петербург', str(year)))

    print('Москва')
    for year in range(2015, 2019):
        print(str(year), money_reader('Средняя зарплата', 'Москва', str(year)))

    print('max spb')
    print(max_money('Средняя зарплата', 'Санкт-Петербург', 2015, 2018))

    print('max zayavok')
    print(region('Количество заявок на потребительские кредиты'))
