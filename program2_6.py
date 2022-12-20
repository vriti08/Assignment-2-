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
a = int(input("first side "))
b = int(input("second side"))
c = int(input("third side "))
if(a+b>c and b+c>a and a+c>b):
    print("the triangle can be formed")

else:
    print("the triangle can not be formed")

