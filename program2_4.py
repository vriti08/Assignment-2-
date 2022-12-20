#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      a
#
# Created:     20-12-2022
# Copyright:   (c) a 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
a = int(input("enter first number    "))
b = int(input("enter second number   "))
c = int(input("enter third number    "))
if(a>=b and a>=c):
   print ("first number is greatest")
elif(b>=c and b>=a):
     print("second number is greatest")
elif(c>=a and c>=b):
     print("third number is greatest")
