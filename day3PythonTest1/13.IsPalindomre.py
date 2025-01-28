def isPalindrome(str):
    for i in range(0,len(str)//2):
        if str[i]!=str[len(str)-1-i]:
            return False
    return True
def main():
    while True:
        str= input("Enter a string")
        if not str=="" :
            if isPalindrome(str):
                print("Palindrome")
            else:
                print("Not a palindrome")
            break
        else:
            print("Enter valid input")
main()