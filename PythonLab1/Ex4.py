def change(str):
    newstr = [str[0].lower()]
    for ch in str[1:]:
        if ch in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            newstr.append('_')
            newstr.append(ch.lower())
        else:
            newstr.append(ch)
     
    return ''.join(newstr)
     
# Driver code
str = input("Your line:")
print(change(str))