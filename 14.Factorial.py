
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def main():
    while True:
        num=int(input("Enter a number to find factorial"))
        if num>=0:
            print(factorial(num))
            break
        else:
            print("Enter valid input")
main()