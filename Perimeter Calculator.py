import math
math.pi

print("1.Perimeter of Square")
print("2.Perimeter of Rectangle")
print("3.Circumference of circle")
print("4.Perimeter of triangle")
print("5.Other closed figure")

choice = int(input("Enter your choice"))
if choice == 1 :
    a = float(input("Enter value of side of square "))
    print("Perimeter of Square is ",4*a)

elif choice == 2 :
    l = float(input("Enter length of rectangle "))
    b = float(input("Enter breadth of rectangle "))
    print("Perimeter of rectangle is ",2*(l+b))

elif choice == 3 :
    r = float(input("Enter radius of circle"))
    print("Circumference of radius is ",2*math.pi*r)

elif choice == 4 :
    a = float(input("Enter length of side 1"))
    b = float(input("Enter length of side 2"))
    c = float(input("Enter length of side 3"))
    print("Perimeter of triangle is ",a+b+c)

elif choice == 5 : 
    print("Please enter more than two value ")
    side = list(map(float, input("Enter all side length separated by space : ").split()))
    print("Perimeter is : ",sum(side))

else :
    print("Invalid choice")