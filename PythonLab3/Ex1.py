def function1(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)


    union_set = set1.union(set2)

    int_set = set1.intersection(set2)

    dif1_set = set1.difference(set2)

    dif2_set = set2.difference(set1)

    lst = [union_set, int_set, dif1_set, dif2_set]

    return lst


lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

print(function1(lst1, lst2))


