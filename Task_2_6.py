# Task 2_6

a = int(input('Введите количество товаров: '))
x = 1
l = list()
name_value = list()
price_value = list()
volume_value = list()
measure_value = list()

while x < a:
    d = {'название': input("Введите НАЗВАНИЕ товара: "), "цена": input("Введите ЦЕНУ товара, руб: "), "количество":
        input("Введите КОЛИЧЕСТВО товара: "), "единица_измерения": input("Введите ЕДИНИЦУ ИЗМЕРЕНИЯ товара: ")}
    name_value.insert(x - 1, d.get('название'))
    price_value.insert(x - 1, d.get('цена'))
    volume_value.insert(x - 1, d.get('количество'))
    measure_value.insert(x - 1, d.get('единица_измерения'))
    t = (x, d)
    l.insert(x, t)
    print('ВВЕДИТЕ ДАННЫЕ СЛЕДУЮЩЕГО ТОВАРА:')
    x += 1
# Далее добавил if, чтобы вывести другое сообщение на выходе
if x == a:
    d = {'название': input("Введите НАЗВАНИЕ товара: "), "цена": input("Введите ЦЕНУ товара, руб: "), "количество":
        input("Введите КОЛИЧЕСТВО товара: "), "единица_измерения": input("Введите ЕДИНИЦУ ИЗМЕРЕНИЯ товара: ")}
    name_value.insert(x, d.get('название'))
    price_value.insert(x, d.get('цена'))
    volume_value.insert(x, d.get('количество'))
    measure_value.insert(x, d.get('единица_измерения'))
    t = (x, d)
    l.insert(x, t)
print('ПОЛУЧИЛСЯ СЛЕДУЮЩИЙ СПИСОК ТОВАРОВ:')
for y in l:
    print(l[l.index(y)])
input('Нажмите Enter, чтобы увидеть общую аналитику по товарам:')
unit_dict = {
    'название': name_value,
    'цена': price_value,
    'количество': volume_value,
    'единица_измерения': measure_value,
}
print(f"Наш Словарь: {unit_dict}")
