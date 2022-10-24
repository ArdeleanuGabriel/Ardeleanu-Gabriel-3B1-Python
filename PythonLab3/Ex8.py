def function8 (d):
    lst= []
    for x in d:
        if x == 'start':
            while d[x] not in lst:
                    lst.append(d[x])
                    x=d[x]
    return(lst)

d = {
  'start': 'a',
  'b': 'a',
  'a': '6',
  '6': 'z',
  'x': '2',
  'z': '2',
  '2': '2',
  'y': 'start'
}

print(function8(d))