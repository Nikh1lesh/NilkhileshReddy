#functions to convert among different units
def CelciusToFahrenheit(celcius):
    return (celcius * 9/5)+32
def FahrenheitToCelcius(fahrenheit):
    return (fahrenheit - 32)*5/9
def celciusTokelvin(celcius):
    return celcius+273
def kelvinToCelcius(kelvin):
    return kelvin-273
def fahrenheitToKelvin(fahrenheit):
    return (fahrenheit-32)*5/9+273
def kelvinToFahrenheit(kelvin):
    return (kelvin-273)*9/5+32
# function to display interface
def interface():
    print("Enter your choice")
    print("1.Celcius to Fahrenheit")
    print("2.Fahrenheit to Celcius")
    print("3.Celcius to Kelvin")
    print("4.Kelvin to Celcius")
    print("5.Fahrenheit to Kelvin")
    print("6.Kelvin to Fahrenheit")
    print("7.Exit")
#main function takes input
def main():
    while True:
        num=int(input("Enter your choice"))
        if num==1:
            n=int(input("Enter value in clecius"))
            ans=CelciusToFahrenheit(n)
            print(f"after conversion: {ans}")
        elif num==2:
            n=int(input("Enter value in Fahrenheit"))
            ans=FahrenheitToCelcius(n)
            print(f"after conversion: {ans}")
        elif num==3:
            n=int(input("Enter value in Celcius"))
            ans=celciusTokelvin(n)
            print(f"after conversion: {ans}")
        elif num==4:
            n=int(input("Enter value in Kelvin"))
            ans=kelvinToCelcius(n)
            print(f"after conversion: {ans}")
        elif num==5:
            n=int(input("Enter value in Fahrenheit"))
            ans=fahrenheitToKelvin(n)
            print(f"after conversion: {ans}")
        elif num==6:
            n=int(input("Enter value in kelvin"))
            ans=kelvinToFahrenheit(n)
            print(f"after conversion: {ans}")
        elif num==7:
            break
        else: 
            print("Enter valid choice")
            
main()

            
    
    
    