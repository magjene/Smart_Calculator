d = {}
s, sign = int, int


def del_num(ind, k=2):
    for _ in range(k):
        del num[ind]


while True:
    s, sign = 0, 1
    num = input()
    if num == '':  # Комманды
        continue
    elif num == '/exit':
        break
    elif num == '/help':
        s = 'The program calculates the sum of numbers'
    elif num[0:1] == '/':
        s = 'Unknown command'
    elif num.isalpha():
        s = d.get(num, 'Unknown variable')
    elif '=' in num:  # Присвоение
        s = None
        num = num.split('=')
        num[0], num[1] = num[0].strip(), num[1].strip()
        if num[0].isalpha() and (num[1].isdecimal() or num[1][1::].isdecimal()):  # Одна буква и цифра
            d.update({num[0]: num[1]})
        elif num[0].isalpha() and num[1].isalpha():  # Оба буквы
            s = d.get(num[1])
            if s is not None:
                d.update({num[0]: s})
                s = None
            else:
                s = 'Unknown variable'
        else:
            s = 'Invalid identifier'
    elif num.isalnum():
        s = 'Invalid identifier'
    else:
        num = list(num)  # Преоброзование
        i = 0
        while len(num) - 1 - i:  # Склейка
            if (num[i].isalpha() and num[i + 1].isalpha()) or (num[i].isdecimal() and num[i + 1].isdecimal()):
                num.insert(i, num[i] + num[i + 1])
                del_num(i + 1)
            else:
                i += 1
        i = 0
        while len(num) - i:  # Склейка минусы
            if i == 0 and num[0] == '-' and num[1].isdecimal():
                num.insert(i, num[i] + num[i + 1])
                del_num(i + 1)
            elif num[i] == '-' and num[i + 1].isdecimal() and num[i - 1] == ' ':
                num.insert(i, num[i] + num[i + 1])
                del_num(i + 1)
        if ' ' in num:  # Удаление пробелов
            while len(num) - 1:
                if num[i] == ' ':
                    del num[i]
                else:
                    i += 1
        for n in num:  # Получение значения одного
            if n.isalpha():
                n = d[n]
            else:


                while '*' in num or '/' in num:
                    i, temp1, temp2, temp = 1, '', '', int
                    if (num[i] == '*' or num[i] == '/') and (i != len(num) - 1):
                        if num[i - 1].isdecimal() or num[i - 1][1::].isdecimal():
                            temp1 = num[i - 1]
                        elif num[i + 1].isdecimal() or num[i + 1][1::].isdecimal():
                            temp2 = num[i + 1]
                        elif num[i - 1].isalpha():
                            temp1 = d.get(num[i - 1])
                        elif num[i + 1].isalpha():
                            temp2 = d.get(num[i + 1])
                        if (temp1 is not None) and (temp2 is not None):
                            if num[i - 1][0] == '-':
                                del num[i - 1][0]
                                sign *= -1
                            if num[i + 1][0] == '-':
                                del num[i + 1][0]
                                sign *= -1
                            if num[i] == '*':
                                temp = int(temp1) * int(temp2) * sign
                            elif num[i] == '/':
                                if temp2 != 0:
                                    temp = int(temp1) // int(temp2) * sign
                                else:
                                    s = 'Divided by zero'
                            del_num(i - 1, 3)
                            num.insert(i - 1, temp)
                            sign = 1

                    i += 1

                try:
                    n1 = int(n)
                except ValueError:  # Определение знака
                    for ni in n:
                        if ni == '-' or ni == '+':
                            if ni == '-':
                                sign *= -1
                        else:
                            s = 'Invalid expression'
                            break
                else:  # Сложение и вычетание
                    s += sign * n1
                    sign = 1
    if s is not None:
        print(s)
print('bye')
