def ISleapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
def main():
    while True:
        year = int(input("Enter year"))
        if year > 0:
            if ISleapYear(year):
                print("Leap year")
            else:
                print("Not a leap year")
            break
        else:
            print("Enter valid input")
            