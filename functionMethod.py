#!/usr/bin/python

def main():
   a = CentOS
   return a

# Function definition is here
def CentOS( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
main()

#mylist = [10,20,30]

#CentOS( mylist )

#print ("Values outside the function: ", mylist)
