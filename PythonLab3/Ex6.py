def function6(*lst):
    unique_set = set()
    duplicate_set = set()
    for x in lst:
        print(x,":")
        if x not in unique_set and x not in duplicate_set:
            unique_set.add(x)
            print("unique primeste", x)
        elif x in unique_set:
            unique_set.remove(x)
            duplicate_set.add(x)
            print("unique pierde si duplicate primeste", x)
    tuplu = tuple((len(unique_set), len(duplicate_set)))
    return tuplu


print(function6("apple", "banana", "cherry", "cherry"))