import utils

while(1):
    a = input("Your number: ")
    if a == "q":
        break
    elif a.isalpha():
        continue
    else:
        a = int(a)
        print("The output: " + str(utils.process_item(a)))