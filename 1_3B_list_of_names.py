# создение первого списка из 100 имен

list1 = []
for i in range(1, 10):
    list1.append(nm.get_first_name())

# создание двух новых списков на основе первого: с именами на букву от А до М и с остальными именами

alphabet = list(map(chr, range(65, 78)))

list2 = []
list3 = []

for i in range(0, len(list1)):
    if list1[i][0] in alphabet:
        list2.append(list1[i])
    else:
        list3.append(list1[i])
print(list1)
print(list2)
print(list3)
