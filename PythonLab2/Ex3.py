def union(lists):
    all_elements = []
    for x in lists:
        all_elements = all_elements + x
    return list(set(all_elements))
 
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def difference(lst1,lst2):
    lst3 = []
    for element in lst1:
        if element not in lst2:
            lst3.append(element)
    return(lst3)

 
lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
print(union([lst1, lst2]))
print(intersection(lst1,lst2))
print(difference(lst1,lst2))
print(difference(lst2,lst1))