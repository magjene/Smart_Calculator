while True:
    s, sign = 0, 1
    num = input()
    if num == '':
        continue
    elif num == '/exit':
        break
    elif num == '/help':
        s = 'The program calculates the sum of numbers'
    elif num[0:1] == '/':
        s = 'Unknown command'
    else:
        num = num.split()
        for n in num:
            try:
                n1 = int(n)
            except ValueError:
                for ni in n:
                    if ni == '-' or ni == '+':
                        if ni == '-':
                            sign *= -1
                    else:
                        s = 'Invalid expression'
                        break
            else:
                s += sign * n1
                sign = 1
    print(s)
print('bye')
