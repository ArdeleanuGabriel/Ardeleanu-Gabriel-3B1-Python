string = input("Enter your string:")
print(string)
counter=0
# Iterate over the string
for ch in string:
    print(ch)
    if ch in ("AEIOUaeiou"):
        counter = counter + 1
print(counter)