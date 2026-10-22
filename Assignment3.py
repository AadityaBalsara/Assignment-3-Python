# Assignment 3: Check for a right-angled triangle using a function
import math
s1 = float(input("Enter length of side 1: "))
s2 = float(input("Enter length of side 2: "))
s3 = float(input("Enter length of side 3: "))
a,b,c=sorted([s1,s2,s3])
if c*c==(b*b)+(a*a) :
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is NOT a right-angled triangle.")
