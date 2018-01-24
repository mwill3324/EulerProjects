def prime():
    num = 600851475143
    i = 2
    while i < num: 
        while num % i == 0: #can be factored
            num = num/i #divide it so its factored
        i = i + 1
    print(num)
prime()


