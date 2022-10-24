def function7(*lst):
    d = dict()
    for x in range(len(lst)):
        for y in range(x,len(lst)):
            if(x != y):
                d.update({'{} | {}'.format(lst[x], lst[y]) : lst[x].union(lst[y]) })
                d.update({'{} & {}'.format(lst[x], lst[y]) : lst[x].intersection(lst[y]) })
                d.update({'{} - {}'.format(lst[x], lst[y]) : lst[x].difference(lst[y]) })
                d.update({'{} - {}'.format(lst[y], lst[x]) : lst[y].difference(lst[x]) })
    return(d)

set1 = set((1,2))
set2 = set((2,3))
set3 = set((3,4))
print(function7(set1,set2,set3))