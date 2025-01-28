def disp(lst):
    for i in lst:
        print(i)
def main():
    print("Enter the number of elements in list")
    n=int(input())
    Odd=[]
    even=[]
    for i in range(n):
        num=int(input())
        if num%2==0:
            even.append(num)
        else:
            Odd.append(num)
    print("Odd numbers")
    disp(Odd)
    print("Even numbers")
    disp(even)       
main()