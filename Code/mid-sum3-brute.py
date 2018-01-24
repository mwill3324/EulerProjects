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


L = []
a = 1
while a < 497:
    L.append(a)
    a = a + 1
L.append(2000)
L.append(3000)
L.append(4000)
random.shuffle(L)

def find(sum,L):
    x = 0
    y = 1
    z = 2
    done = False
    while x < len(L):
        if done == True:
            break
        y = 1
        while y < len(L):
            if done == True:
                break
            z = 2
            while z < len(L):
                temp = L[x] + L[y] + L[z]
                if temp == sum:
                    print (sum, '=', L[x], '+', L[y], '+', L[z])
                    done = True
                    break
                z = z + 1
            y = y + 1
        x = x + 1

time_begin = time.process_time()

find(9000,L)
time_delta = time.process_time() - time_begin
print("Time = %.6f sec" % time_delta)