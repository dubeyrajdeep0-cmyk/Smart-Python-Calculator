import math
math.pi

print("1.Area of circle")
print("2.Area of reactangle")
print("3.Area of Square")
print("4.Area of triangle")
print("5.Area of Parallelogram")
print("6.Area of Trapezium")

choice = int(input("Enter your choice"))

if choice == 1 :
    r = float(input("Enter radius of circle"))
    print("Area of circle is ",math.pi*r*r)

elif choice == 2 :
    l = float(input("Enter length of rectangle "))
    b = float(input("Enter breadth of rectangle "))
    print("Area of rectangle is ",l*b)

elif choice == 3 :
    a = float(input("Enter value of side of square "))
    print("Area of Square is ",a*a)

elif choice == 4:
    b = float(input("Enter base length of triangle "))
    h = float(input("Enter height of triangle "))
    print("Area of triangle is ",(b*h)/2)

elif choice == 5:
    b = float(input("Enter base length of parallelogram "))
    h = float(input("Enter height of parallelogram "))
    print("Area of parallelogram is ",b*h)

elif choice == 6 :
    a = float(input("Enter length of first base "))
    b = float(input("Enter length of second base "))
    h = float(input("Enter height of trapezium "))
    print("Area of trapezium is "((a+b)*h)/2)

else :
    print("Invalid choice")