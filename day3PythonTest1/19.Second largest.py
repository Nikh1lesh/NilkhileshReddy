def InputAndSecondLargest():
    print("Enter the number of elements in list")
    
    n = int(input())
    for i in range(n):
        num = int(input())
        lst.append(num)
    lst.sort()
    print("Second largest element is", lst[-2])
def main():
    global lst
    lst = []
    InputAndSecondLargest()
    
main()
    
    