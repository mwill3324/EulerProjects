def fib():
    sum =0
    x=1
    y=x
    while x < 4000000:
        if x%2 == 0:
            sum = sum + x
        temp = x
        x = x + y
        y = temp
    print(sum)
fib()