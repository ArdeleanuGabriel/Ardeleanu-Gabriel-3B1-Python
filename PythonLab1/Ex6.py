def isPalindrome(s):
    return s == s[::-1]



x = input("Enter your number:")

if(isPalindrome(x)):
    print("The number is palindrome.")
else:
    print("The number is NOT palindrome.")
