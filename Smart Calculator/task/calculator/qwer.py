a = list('123 4!asd ert6984')
b = []
for i in range(len(a)-1, 0, -1):
    if a[i] == ' ':
        del a[i]
print(a)
i = 0
while True:
    if (a[i].isalpha() and a[i + 1].isalpha()) or (a[i].isdecimal() and a[i+1].isdecimal()):
        a.insert(i, a[i] + a[i + 1])
        del a[i + 1]
        del a[i + 1]
    else:
        b.append(a[i])
        i += 1
    n = len(a) - 1
    if n <= i:
        break
print(a)
