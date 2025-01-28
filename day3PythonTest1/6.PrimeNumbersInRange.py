import math
#function is check if a number is prime
def IsPrime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    c=0;
    for i in range(3,int(math.sqrt(n))+1):
        if n%i==0:
            c+=1
    if c<1:
        return True
    return False
#function to print prime numbers in the range[a,b]
def printPrime(a,b):
    for i in range(a,b+1):
        if IsPrime(i):
            print(i)
# main function
def main():
    while True:
        a=int(input("Enter the starting number of the range"))
        b=int(input("Enter the ending number of the range "))
        if a>0 and b>0 and b>a:
            printPrime(a,b)
            break
        else:
            print("Enter valid input")
        
main()
    
    
        