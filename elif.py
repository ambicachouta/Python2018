#3. ELIF STATEMENT :

perl=50
python=80

if (perl>python):
    print ("Perl Course fee is more than python fee")
elif(perl==python):
    print ("Perl course fee is less than python fee")
elif(perl<python):
    print ("Perl course fee is equal to python fee")
elif(perl!=python):
    print ("Perl course fee is not less than python fee")
else:
    print ("None of the above are matched")

print ("We are out of the if..elif block")
