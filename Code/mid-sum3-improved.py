"""
Test 1
Input: sum = 19, L = [33, 22, 11, 7, 3, 66, 3, 2, 14, 24, 23, 15, 20, 10, 5, 9].
Expected output: 19 = 11 + 3 +5
Output: 19 = 11 + 3 +5
Test 2
Input: sum = 120, L = [72, 96, 57, 32, 61, 66, 60, 29, 45, 67, 58, 27, 35, 29, 73].
Expected output: 120 = 32 + 61 + 27
Output: 120 = 32 + 61 + 27
Test 3
Input: sum = 40, L = [92 , 11, 67, 95, 89, 55, 4, 27, 9, 43, 61, 92, 73, 37, 88].
Expected output: 40 = 4 + 27 + 9
Output: 40 = 4 + 27 + 9
Test 4
input: sum = 9000, L =  [rand(1…497, 2000, 3000, 4000)]
Expected output: 9000 = 2000 + 3000 + 4000 (in whatever order due to randomization)
Output: 9000 = 4000 + 3000 + 2000
Marcus Williams
"""
import time
import random
List = []
a = 1
while a < 497:
    List.append(a)
    a = a + 1
List.append(2000)
List.append(3000)
List.append(4000)
random.shuffle(List)

def bub(List):
    for passnum in range(len(List)-1,0,-1):
        for i in range(passnum):
            if List[i]<List[i+1]:
                temp = List[i]
                List[i] = List[i+1]
                List[i+1] = temp

def find(Sum, List):
    for i,a in enumerate(List):
        x = 1
        y = len(List)-1
        if a > Sum:
            x = x + 1
            continue
        done = False
        while x < y and done != True:
            if x == i:
                x = x + 1
            if a + List[x] + List[y] == Sum:
                print(Sum, "=", a, "+",List[x],"+", List[y])
                return
            if Sum < (a + List[x] + List[y]) and a + List[x] + List[y] != Sum:
                if(x == 0):
                    y = y + 1
                else:
                    x = x + 1
            if Sum > (a + List[x] + List[y]) and a + List[x] + List[y] != Sum:
                if y == len(List):
                    x = x + 1
                else:
                    y = y - 1
time_begin = time.process_time()
bub(List)
find(9000,List)
time_delta = time.process_time() - time_begin
print("Time = %.6f sec" % time_delta)



L = []
a = 1
while a < 497:
    L.append(a)
    a = a + 1
L.append(2000)
L.append(3000)
L.append(4000)
random.shuffle(L)

def find2(sum,L):
    x = 0
    y = 1
    z = 2
    done = False
    while x < len(L):
        if done == True:
            break
        y = x+1
        while y < len(L):
            if done == True:
                break
            z = y +1
            while z < len(L):
                temp = L[x] + L[y] + L[z]
                if temp == sum:
                    print (sum, '=', L[x], '+', L[y], '+', L[z])
                    done = True
                    break
                z = z + 1
            y = y + 1
        x = x + 1
time_begin1 = time.process_time()

find(9000,L)
time_delta1 = time.process_time() - time_begin1
print("kevins way")
print("Time2 = %.6f sec" % time_delta1)

#combination_in_range(5,List)