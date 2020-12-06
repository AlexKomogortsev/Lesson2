# Task 2_5

l = [7, 6, 3, 2, 2, 2]
a = int(input('Введите натуральное число: '))

if a > l[-1]:
    for x in l:
        if a > x:
            l.insert(l.index(x), a)
            break
        elif a == x:
            l.insert(l.index(x) + 1, a)
            continue
        else:
            continue
else:
    l.append(a)
print(l)
