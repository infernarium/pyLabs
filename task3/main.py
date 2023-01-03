import ctypes
import sys

# Загрузка библиотеки
test = ctypes.CDLL('./libtest.dll')

a = input()
show_lycherl_candidates(a)

