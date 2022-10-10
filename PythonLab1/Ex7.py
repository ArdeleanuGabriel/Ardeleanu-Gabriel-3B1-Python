str = input("Enter your string:")
nr = []
foundNumber = False
for ch in str:
    if (ch.isdigit()):
        foundNumber = True
        nr.append(ch)
    elif (ch.isalpha() & foundNumber == True):
        break

print(''.join(nr))