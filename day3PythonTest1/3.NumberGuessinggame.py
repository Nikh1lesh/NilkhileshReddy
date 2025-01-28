import random
#function to generate random number
def generateRandom():
    rnum=random.randint(1,100)
    return rnum

#function to check if the guessed number is correct
def guessRnum(rnum,num):
    if num==rnum:
        return True
    else:
        return False
def hint(rnum,num):
    if num>rnum:
        print("Your guess is highr")
    else:
        print("Your guess is low")
#main function
def main():
    rnum=generateRandom()
    while True:
        num=int(input("Enter your Guess"))
        if num>100 or num<1:
            print("Enter valid guess between 0 to 100")
        elif not guessRnum(rnum,num):
            hint(rnum,num)
            print("Try again")
        elif guessRnum(rnum,num):
            print("Your guess is correct")
            break
       
main()
        