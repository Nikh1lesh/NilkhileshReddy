bal = 10000 #Assuming initial balance is 10000
#Function to check balance
def checkBalance():
    global bal;
    return bal
#Functoin to withdraw 
def withdrawAmount():
    global bal
    while True:
        
        amount=int(input("Enter the amount to be withdrawn"))
        if amount>0:                                    #validating input
            if amount<=bal:
                bal=bal-amount
            else:
                print("Insufficient balance")
        else :
            print("Enter valid input")
                
#Function to depopsit   
def depositAmount():
    global bal
    while True:
        amount=int(input("Enter the amount ot be deposited"))
        if amount>0:
            bal=bal+amount
        else:
            print("Enter valid input")
#Function to display interface
def interface():
    print("1.Check Balance")
    print("2.Withdraw Money")
    print("3.Deposit Money")
    print("4.Exit")
def main():
    
    while True:
        interface()
        n=int(input("Enter your choice"))
        if n==1:
            print(checkBalance())
            
        elif n==2:
            withdrawAmount()
            
        elif n==3:
            depositAmount()
            
        elif n==4:
            Print("Thank you")
            break
        else: 
            break

main()