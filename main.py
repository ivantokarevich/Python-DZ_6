""" Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов'] """



""" list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

lenght: int = len(list1)
store_id = id(list1)
for i in range(lenght):
    entity = list1.pop(0)
    if  entity.isdigit():
        list1.append(F'"{int(entity):02d}"')
    elif entity[0] == "+" and entity[1].isdigit():
        list1.append(F'"+{int(entity):02d}"')
    else:
        list1.append(entity)
print(' '.join(list1)) """


""" Дан список, содержащий искажённые данные с должностями и именами сотрудников: ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита'] """


""" hi = 'Привет, {}!'

incorrect_staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for correct_staff in incorrect_staff:
    print(hi.format(correct_staff.split()[-1].title())) """


""" Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...] """




list = [57.8, 46.51, 97, 66, 19.48, 83, 33.11, 55, 7.77, 49]

store_id = id(list)
print(f"{'a':-^79}")
end_word: str = ", "

for i, num in enumerate(list):

    fix_price = str(f"{float(num):.2f}").split(".")

    if i == len(list) - 1:
        end_word = "\n"

    print(f"{fix_price[0]} руб {fix_price[1]} коп", end=end_word)


print(f"{'b':-^79}")
print(f"id перед сортировкой {store_id}")
list.sort()
print(list)
print(f"id после сортировки {id(list)}")

print(f"{'c':-^79}")

copy_of_list = list.copy()
copy_of_list.sort(reverse=True)

print(copy_of_list)
print(store_id)
print(id(copy_of_list))


print(f"{'d':-^79}")
print("Цены пяти самых дорогих товаров", list[-6:-1])