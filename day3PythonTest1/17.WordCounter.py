def countWords(s):
    count=0
    for i in s:
        if i==' ':
            count+=1 
    return count+1
def main(): 
    while True:
        s = input("Enter a string")
        if not s=="":
            print(f"Number of words in the string are {countWords(s)}")
            break
        else:
            print("Enter valid input")
main()
