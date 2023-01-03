
import csv
import split_module
import statistics
import sys

def read_data_from_file(filename):
    '''
    Функция для считывания данных из файла csv
    Параметры: file - открытый csv файл
    Возвращаемое значение: список полученных строк
    '''
    with open(filename) as file:
        list = []
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            list.append(line)
        return list

def calculate_statistics(period):
    '''
    Функция для подсчета статистики
    Параметры: period - данные за период в виде:
    [время1, число1],
    [время2, число2], ...
    Возвращаемое значение: список значений в виде:
    [длина, среднее, мода, медиана]
    '''
    stat = []
    num = []
    for line in period:
        num.append(int(line[1]))
    length = len(num)
    mean = statistics.mean(num)
    try:
        mode = statistics.mode(num)
    except statistics.StatisticsError:
        mode = 'undefined'
    median = statistics.median(num)
    stat += [length, mean, mode, median]
    return stat

def main():
    '''
    Главная функция
    '''
    if len(sys.argv) != 3:
        print("Ошибка: неверное кол-во аргументов!")
        return
    filename = sys.argv[1]
    time = int(sys.argv[2])
    data = read_data_from_file(filename)
    split = split_module.split_data(data, time)
    for period in split:
        start = period[0][0]
        end = period[-1][0]
        stat = calculate_statistics(period)
        print(f"start = {start}, end = {end}:")
        print(f"    length = {stat[0]}, mean = {stat[1]}, mode = {stat[2]}, median = {stat[3]}")

if __name__ == '__main__':
    main()

