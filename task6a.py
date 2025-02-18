def hourglass(num):
    l1 = []
    outer = 0
    inner = (2 * num)  - 5
    
    for i in range(num, 0, -1):
        if i == num or i == 1:
            l1.append(' ' * outer + '*' * ((2 * i) - 1))
            outer += 1
        else:
            l1.append(' ' * outer + '*' + ' ' * inner + '*')
            outer += 1
            inner -= 2
    for i in l1:
        print(i)
    for i in reversed(l1):
        print(i)

hourglass(6)
