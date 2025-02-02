#function to print multiplication table
def generate(num,range):
    for i in range(1,int(r)+1):
        ans=i*n
        print(f"{n} * {i} = {ans}")
        
def main():
    while True:
        num=int(input("Enter a number to generate multiplication table"))
        range=int(input("Enter the range"))
        if r>=1 and isinstance(range,int) and isinstance(num,int): #validating input
            generate(num,range)
            break;
        else:
            print("Enter valid input")
            
main()
    