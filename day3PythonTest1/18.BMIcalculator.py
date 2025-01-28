def calculateBMI(weight, height):
    return weight/(height * height)
def category(bmi):
    if bmi<18.5:
        return "Underweight"
    elif bmi<25:
        return "Normal"
    elif bmi<30:
        return "Overweight"
def main():
    while True:
        weight = float(input("Enter your weight"))
        height = float(input("Enter your height"))
        if weight>0 and height>0:
            bmi = calculateBMI(weight, height)
            print(f"Your BMI is {bmi}")
            print(f"You are {category(bmi)}")
            break
        else:
            print("Enter valid input")
        
main()