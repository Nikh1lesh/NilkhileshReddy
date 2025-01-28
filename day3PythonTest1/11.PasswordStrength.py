def checkSCharcters(str):
    d=0
    u=0
    l=0
    s=0
    for i in range(0,len(str)):
        if str[i].isdigit():
            d+=1
        elif str[i].isupper():
            u+=1
        elif str[i].islower():
            l+=1
        elif not str[i].isalnum():
            s+=1
    return (d,u,l,s)
def checkstrength(d,u,l,s):
    if d>0 and u>0 and l>0 and s>0:
        return True
    else:
        return False
def main():
    while True:
        str= input("Enter a string")
        if not str=="" :
            (d,u,l,s)=checkSCharcters(str)
            if checkstrength(d,u,l,s) and len(str)>=8:
                print("Password is strong")
            else:
                print("Password is weak")
            break
        else:
            print("Enter valid input")
main()
    