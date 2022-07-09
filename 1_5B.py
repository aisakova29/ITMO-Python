# первое задание

def func(*args):
    counter = 0
    _sum = 0
    for num in args:
        if num == 'none':
            continue
        _sum += num
        counter += 1
    return round(_sum / counter, 2)

func(4, 'none', 6, 'none', 5)

# второе задание

def func(*args):
    list1 = []
    list2 = []
    for num in args:
        if num > 0:
            list1.append(num)
        else:
            list2.append(num)
    return sorted(list1), sorted(list2, reverse=True)

func(4, -4, 8, -3, 5)


# третье задание

def func(num, exp):
    return(num ** exp)

func(3, 3)

def func(num, exp):
    if (exp == 1):
        return (num)
    if (exp != 1):
        return (num * func(num, exp - 1))

func(3, 3)		
