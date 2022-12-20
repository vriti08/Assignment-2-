#-------------------------------------------------------------------------------
# Name:        module1
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
name=str(input("Enter your Name : "))
SID=int(input("Enter your SID : "))
department=str(input("Department : "))
CGPA= 9.0

print("\n\nHey, %s Here! \nMy SID is %d\nI am from %s department and my CGPA is %f " % (name,SID,department,CGPA))