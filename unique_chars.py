import sys
a=input("Enter a string to determine if it has unique characters\n")
mask=[0]*256
for i in a:
    n=ord(i)
    if (mask[n]==0):
        mask[n]=1
    else:
        print ("The string does not have unique characters")
        sys.exit(0)

print ("The string has unique characters")

    
