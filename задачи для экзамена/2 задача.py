from itertools import permutations

arr = [1,2,3,4]
arr.sort(reverse = True)
mylist = list(permutations(arr))
for h1,h2,m1,m2 in mylist:
    hrs = h1 * 10 + h2
    mins = m1 * 10 + m2

    if hrs < 24 and mins < 60:
        print (str(hrs)+':'+str(mins))
        break
    

