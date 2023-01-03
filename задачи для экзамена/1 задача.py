def primal(number):
    for i in range(2,int(number/2)):
        if (number % i)!=0:
            continue
        else:
            return 0
    return 1

def palindrom(number):
    if str(number) == str(number)[::-1]:
        return 1
    else:
        return 0

n = int(input())
i=n

while 1:
    if ((palindrom(i)) and (primal(i))):
        print(i)
        break
    else:
        i += 1
    


