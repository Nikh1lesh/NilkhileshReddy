def isVowel(ch):
    if ch=='i' or ch=='o'or ch=='a' or ch=='e' or ch=='u':
        return True
    return False
def isConsonant(ch):
    if not isVowel(ch) and not ch.isdigit() and ch.isalnum():
        return True
    else:
        return False
def count(string):
    con=0
    special=0
    vow=0
    digit=0
    for i in range(0,len(string)):
        if isConsonant(string[i]):
            con+=1
        elif isVowel(string[i]):
            vow+=1
        elif string[i].isdigit():
            digit+=1
        elif not string[i].isalnum():
            special+=1
    return (vow,con,digit,special)
    

def display(vowels,consonants,digits,special,rev):
    print(f"vowels={vowels}")
    print(f"consonants={consonants}")
    print(f"digits={digits}")
    print(f"special={special}")
    print(f"Reversed string={rev}")
def main():
    while True:
        string= input("Enter a string")
        if not string=="" :
            
            (vowels,consonants,digits,special)=count(string)
            rev=string[::-1]
            display(vowels,consonants,digits,special,rev)
            break
    else:
        print("Enter valid input")
    
main()
    
    
            
            