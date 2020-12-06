# Task 4

s = input('Введите несколько слов, разделяя их пробелами: ')
l = s.split()

for x in l:
    if len(x) <= 10:
        print(l.index(x) + 1, x)
    else:
        print(l.index(x) + 1, x[:10:])
