def aidana_list(a):
    for i in a:
        if i % 2 != 0: a.remove(i)
    return a
print(aidana_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

