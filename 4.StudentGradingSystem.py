
#function to calculate total,percentage
def calculate(a,b,c,d,e):
    total=int(a+b+c+d+e)
    percentage=total/500*100
    return (total,percentage)
#function to give grade
def grade(p):
    if p>=90:
        return "A"
    elif p>=80 and p<70:
        return "B"
    elif p>=60 and p<70:
        return "C"
    elif p>=70 and p<40:
        return "D"
    else:
        return "F"
#functoin to print result
def display(name,total,percentage,grade):
    print("stuedent name is",name)
    print("Total marks is",total)
    print("Percentage is",percentage)
    print("Grade is",grade)
#main function
def main():
    while True:
        name=input("Enter your name")
        sub1=int(input("Enter subject1 marks"))
        sub2=int(input("Enter subject2 marks"))
        sub3=int(input("Enter subject3 marks"))
        sub4=int(input("Enter subject4 marks"))
        sub5=int(input("Enter subject5 marks"))
        if name != "" and sub1>0 and sub2>0 and sub3>0 and sub>40 and sub5>0:
            (total,percentage)=calculate(sub1,sub2,sub3,sub4,sub5)
            g=grade(percentage)
            display(name,total,percentage,g)
            break
        else:
            print("Enter valid input")
main()