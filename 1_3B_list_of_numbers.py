from random import randint as rnd

random_list = []
x = 28

for i in range (0, 100):
    random = rnd(1, 100)
    random_list.append(random)


random_list2 = []
for i in range (0, len(random_list)):
    if random_list[i] > x:
        random_list2.append('High')
    elif random_list[i] < x:
        random_list2.append('Low')
    else:
        random_list2.append('Equal')

print(random_list)
print(random_list2)
