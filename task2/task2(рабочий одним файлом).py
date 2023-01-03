import csv
import sys
import statistics
import os.path

ls = []

if (len(sys.argv))<2 or (len(sys.argv))>3 : #исключение при недостаточном/избыточном кол-ве аргументов
    print('using: task2.py filename.csv minutes')
    exit()

file = sys.argv[1]

if not(os.path.isfile(file)): #исключение при несуществующем файле
    print('Файла с именем "'+file+'" не существует')
    exit()

try: #исключение при неверном указании времени(как это возможно?)
    time = int(sys.argv[2])
except:
    print("Время указано в неверном формате")
    exit()

def read_data_from_file(filename, output_massive):
    '''
    using: read_data_from_file(str filename, char massive_to_fill[][])
    return char massive[][]
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
    '''
    statistic_ = []
    for under_massive in massive:
        
        helper_massive = []
        
        helper_massive.append(under_massive[0])                 #1 временной отрезок

        under_massive.remove(under_massive[0])
        
        helper_massive.append(len              (under_massive)) #2 длина
        helper_massive.append(statistics.mean  (under_massive)) #3 среднее арифметическое
        helper_massive.append(statistics.mode  (under_massive)) #4 мода
        helper_massive.append(statistics.median(under_massive)) #5 медиана
        
        statistic_.append(helper_massive)
        
    return statistic_

time = time * 60

read_data_from_file(file, ls)
ls = split_data(time, ls)
statist = statistic(ls)

print('Статистика:')

for i in statist:
    print('С '+str(int(i[0]/time-1)*time)+' до '+str(i[0])+' секунды len:'+str(i[1])+'; mean:'+str(i[2])+'; mode:'+str(i[3])+'; median:'+str(i[4]))
