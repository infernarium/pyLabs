'''
модуль чтения, разбиения и подсчета статистики из csv файла
'''

import csv
import statistics


def read_data_from_file(filename, output_massive):
    '''
    using: read_data_from_file(str filename, char massive_to_fill[][])
    return char massive[][]
    функция построчного разбиения файла на массивы вида [время, значение]
    '''
    
    massive = []
    
    with open(filename, newline="\n") as file:
        reader = csv.reader(file)
        for row in reader:
            massive.append(row)

    for i in range(1,len(massive)):
        output_massive.append(str(massive[i][0]) + "," + str(massive[i][1]))

    return output_massive


def split_data(time, file):
    '''
    using: split_data(char massive[][], int minutes)
    return int massive[][]
    функция разбивает прочитанные данные на отрезки, с сохранением крайнего значения времени
    '''
    n = 1
    output_massive = []
    under_massive = [time]
    
    for string in file:
        if (float(string.split(",")[0]) > time * n):
            output_massive.append(under_massive)
            n = n + 1
            under_massive = [time * n]
        under_massive.append(int(string.split(",")[1]))
        
    output_massive.append(under_massive)
    return output_massive


def statistic(massive):
    '''
    using: statistic(char massive[][])
    return (int massive [][interval, len, mean, mode, median])
    функция высчитывает статистику по временным отрезкам
    '''
    statistic_ = []
    for under_massive in massive:
        
        helper_massive = []
        
        helper_massive.append(under_massive[0])                 #1 временной отрезок

        under_massive.remove(under_massive[0])
        
        helper_massive.append(len(under_massive))               #2 длина
        helper_massive.append(statistics.mean(under_massive))   #3 среднее арифметическое
        helper_massive.append(statistics.mode(under_massive))   #4 мода
        helper_massive.append(statistics.median(under_massive)) #5 медиана
        
        statistic_.append(helper_massive)
        
    return statistic_
