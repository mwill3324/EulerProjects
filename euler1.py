
def problem1():
    sum = 0
    x = 1
    for x in range(1,1000):
        if x%3==0 or x%5==0:
            sum = sum + x
    print (sum)
problem1()