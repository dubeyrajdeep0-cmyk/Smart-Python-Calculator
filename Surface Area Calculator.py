import math
math.pi
print("1.Cube")
print("2.Cuboid")
print("3.Sphere")
print("4.Cylinder")
print("5.Cone")

choice = int(input("Enter your choice "))

if choice == 1 :
    s = float(input("Enter side of Cube "))
    print("Surface Area of Cube is ",6*s*s)

elif choice == 2:
    l = float(input("Enter length of the Cuboid "))
    b = float(input("Enter breadth of the Cuboid "))
    h = float(input("Enter height of the Cuboid "))
    print("Surface Area of Cuboid is ",2*(l*b + b*h + h*l))

elif choice == 3 :
    r = float(input("Enter radius of the Sphere "))
    print("Surface Area of Sphere is ",4 * math.pi * r * r)

elif choice == 4 :
    r = float(input("Enter radius of Cylinder "))
    h = float(input("Enter height of Cylinder "))
    print("Surface Area of Cylinder is ", 2 * math.pi * r*(r + h))

elif choice == 5 :
    r = float(input("Enter radius of Cone "))
    l = float(input("Enter slant height of Cone "))
    print("Surface Area of Cone is ",math.pi * r*(r + l))

else :
    print("Invalid choice")