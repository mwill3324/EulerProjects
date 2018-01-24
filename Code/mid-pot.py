case = 1
while(True):
    print("Case",case)
    t = True
    n = input()
    n = int(n)
    list=[]
    i = 0
    if n is 0:
        break
    while i < n:
        list.append(int(input()))
        i = i + 1
        print(list)
    while t == True:
        temp = 0
        line=input()
        x = line.split(' ')
        a = x[0]
        if a == 'END':
            case = case + 1
            t = False
            break
        else:
            b = int(x[1])
            c = int(x[2])

        print (a,b,c)


        if a is 'm':
            p = b
            while p <= c:
                temp += list[p]
                p = int(p) + 1
            print(temp)

        if a is 's':
            list[b] = c