import sys
import os.path
import CSVstatistics

ls = []

#исключение при недостаточном/избыточном кол-ве аргументов
if len(sys.argv)<=2 or len(sys.argv)>3 : 
    print('using: task2.py filename.csv minutes')
    exit()

file = sys.argv[1]

#исключение при несуществующем файле
if not(os.path.isfile(file)): 
    print('Файла с именем "'+file+'" не существует')
    exit()

#исключение при неверном указании времени(как это возможно?)
try:
    time = int(sys.argv[2]) * 60
except:
    print("Время указано в неверном формате")
    exit()

CSVstatistics.read_data_from_file(file, ls)
print(ls)
ls = CSVstatistics.split_data(time, ls)
statist = CSVstatistics.statistic(ls)
'''
print('Статистика:')

for i in statist:
    print('С '+str(int(i[0]/time-1)*time)+' до '+str(i[0])+' секунды len:'+str(i[1])+'; mean:'+str(i[2])+'; mode:'+str(i[3])+'; median:'+str(i[4]))
'''
