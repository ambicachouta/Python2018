count=0
name = input('Enter your Name to find number of Vowels in your name : ')
for letter in name:
    if (letter in ['A','E','I','O','U','a','e','i','o','u']):
        count=count+1

print ("You have", count, "Vowels in your name")
