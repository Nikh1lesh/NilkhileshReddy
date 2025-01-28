#function to check age
def checkage(age):
    if(age<21):
        return False
    return True
#function to check salary
def checkSalary(salary):
    if(salary<30000):
        return False
    return True
#function to check creditscore
def checkCreditScore(score):
    if(score<600):
        return False
    return True
#function to check eligibility
def checkEligibilty(age,salary,score):
    if checkage(age):
        if checkSalary(salary):
            if checkCreditScore(score):
                print("Your loan is approved")
            else:
                print("your loan is rejected as it Doesn't meet the minimum creditScore criteria")
        else:
            print("your loan is rejected as it Doesn't meet the minimum salary criteria")
    else:
        print("your loan is rejected as it Doesn't meet the minimum age criteria")
#function to validate input
def validateInput(age,salary,score):
    if isinstance(age,int) and isinstance(age,int) and isinstance(age,int) and age>0 and salary>0 and score>0:
        return True
    else:
        return False

#main Function
def main():
    while True:
        
        age=int(input("Enter your age"))
        salary= int(input("Enter your salary"))
        score=int(input("Enter your credit scrore"))
        if validateInput(age,salary,score):
            checkEligibilty(age,salary,score)
            break
        else:
            print("Enter valid Input")
            
            
main()