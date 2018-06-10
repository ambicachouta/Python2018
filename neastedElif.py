"""
3. NESTED IF-ELSE STATEMENT :

>>> ord('A')
65
>>> ord("Z")
90
>>> ord('a')
97
>>> ord("z")
122
"""
char=input("Please enter any charcter : ")

if ord(char)>=65 and ord(char)<=90:
    print ("You entered an upper case alphabet")
    if char in ['A','E','I','O','U']:
        print ("You entered A vowel.",char)
    else:
        print ("You entered a consonant.", char)
elif ord(char)>=97 and ord(char)<=122:
    print ("You entered an Lower case alphabet")
    if char in ['a','e','i','o','u']:
        print ("You entered a vowel.",char)
    else:
        print ("You entered a consonant.",char)
else:
    print (char,"You did not enter an alphabet.")
print ("We are out of the if..elif block")
