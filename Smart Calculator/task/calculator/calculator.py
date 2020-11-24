d = {}
s, sign, temp1, temp2, temp_s = int, 1, int, int, ''


def computer(t):
    temp_add = []
    act = ''
    for j1 in t:
        if act is '':
            temp_add.append(j1)
        elif act == '*':
            temp_add.pop()
            k = temp_add.pop()
            if isinstance(k, int) and isinstance(j1, int):
                temp_add.append(k * j1)
            else:
                return 'Invalid expression'
            act = ''
        elif act == '/':
            if j1 != 0:
                temp_add.pop()
                k = temp_add.pop()
                if isinstance(k, int) and isinstance(j1, int):
                    temp_add.append(k // j1)
                else:
                    return 'Invalid expression'
                act = ''
            else:
                return 'Divided by zero'
        if j1 == '*':
            act = '*'
        elif j1 == '/':
            act = '/'
    s_out = 0
    sign_out = 1
    for nu in temp_add:
        if nu == '-' or nu == '+':
            if nu == '-':
                sign_out *= -1
        else:
            if isinstance(nu, int):
                s_out += nu * sign_out
                sign_out = 1
            else:
                return 'Invalid expression'
    return s_out


while True:
    temp = []
    s, sign = 0, 1
    num = input().strip()
    if num == '':  # Комманды
        continue
    elif num == '/exit':
        break
    elif num == '/help':
        s = '''The program calculates
addition and subtraction
3 ++2---1  # equals 4
multiplication, division
3 *2/ 3 + 1  # equals 3
unary minus
5+ -2 * 4  # equals -3
operation with parentheses ( )
5+(4-2)*4 + -1  # equals 12
operations with variables
n=5
kl=1
n  # equals 5
(n * kl)* 2 +1  # equals 11
'''
    elif num[0:1] == '/':
        s = 'Unknown command'
    elif num.isalpha():
        s = d.get(num, 'Unknown variable')
    elif '=' in num:  # Присвоение
        s = None
        num = num.split('=')
        num[0], num[1] = num[0].strip(), num[1].strip()
        if num[0].isalpha() and (num[1].isdecimal() or num[1][1::].isdecimal()):  # Одна буква и цифра
            d.update({num[0]: int(num[1])})
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
        num.insert(0, ' ')
        num.append(' ')
        for i in range(1, len(num) - 1):  # Склейка
            if num[i] == '(' or num[i] == ')' or num[i] == '*' or num[i] == '/':
                temp. append(num[i])
            elif (num[i].isdecimal() or (num[i] == '-' and (num[i - 1] == ' ' or num[i - 1] == '(')))\
                    and num[i + 1].isdecimal():
                if num[i] == '-':
                    temp_s = '-'
                    for j in range(i - 1, 0, -1):
                        if num[j] == ' ':
                            continue
                        elif num[j] == '-' or num[j] == '+' or num[j] == '/' or num[j] == '*' or num[j] == '(':
                            break
                        else:
                            temp_s = ''
                            break
                else:
                    temp_s += num[i]
            elif num[i].isdecimal() and not num[i + 1].isdecimal():
                temp_s += num[i]
                temp.append(int(temp_s))
                temp_s = ''
            elif num[i].isalpha() and num[i + 1].isalpha():
                temp_s += num[i]
            elif num[i].isalpha() and not num[i + 1].isalpha():
                temp_s += num[i]
                s = d.get(temp_s, 'Unknown variable')
                if s != 'Unknown variable':
                    temp.append(s)
                temp_s = ''
            elif (num[i] == '+' or num[i] == '-') and (num[i + 1] == '+' or num[i + 1] == '-'):
                if num[i] == '-':
                    sign *= -1
            elif (num[i] == '+' or num[i] == '-') and (num[i + 1] != '+' or num[i + 1] != '-'):
                if num[i] == '-':
                    sign *= -1
                temp.append('+') if sign == 1 else temp.append('-')
                sign = 1
        while True:
            num = []
            ind_l, ind_r = None, None
            for i, val in enumerate(temp):
                if val == '(' and ind_r is None:
                    ind_l = i
                elif val == ')' and ind_r is None:
                    ind_r = i
            if ind_l is None and ind_r is None:
                s = computer(temp)
                break
            elif isinstance(ind_l, int) and isinstance(ind_r, int) and ind_r > ind_l:
                del temp[ind_l]
                for _ in range(ind_r - ind_l - 1):
                    num.append(temp.pop(ind_l))
                del temp[ind_l]
                temp.insert(ind_l, computer(num))
            else:
                s = 'Invalid identifier'
                break
    if s is not None:
        print(s)
#     ---------------------------------------------------
#     print(temp)
#     temp = []
#         ---------------------------------------------------
print('bye')
