import random


def listoverlap(list1, list2):
    '''list3 = []
    for i in list1:
        if i in list2:
            if i not in list3:
                list3.append(i)
    return list3'''
    return list(set(list1).intersection(list2))


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    d = random.sample(range(30), 12)
    e = random.sample(range(30), 12)
    c = listoverlap(a, b)
    print(c)
    return


if __name__ == '__main__':
    main()
