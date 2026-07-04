import math
math.pi
print("1.Cube")
print("2.Cuboid")
print("3.Cone")
print("4.Sphere")
print("5.Cylinder")
choice = int(input("Enter your choice"))

if choice == 1 :
    s = float(input("Enter value of side of cube "))
    print("Volume of cube is ",s*s*s)

elif choice == 2 :
    l = float(input("Enter length of cuboid "))
    b = float(input("Enter breadth of cuboid "))
    h = float(input("Enter height of cuboid "))
    print("Volume of cuboid is ",l*b*h)

elif choice == 3 :
    r = float(input("Enter radius of cone "))
    h = float(input("Enter heigth of cone "))
    print("Volume of cone is ",(math.pi*r*r*h)/3)

elif choice == 4 :
    r = float(input("Enter radius of sphere "))
    print("Volume of sphere is ",(4*math.pi*r*r*r)/3)

elif choice == 5 :
    r = float(input("Enter radius of cylinder "))
    h = float(input("Enter height of cylinder "))
    print("Volume of cylinder is ",math.pi*r*r*h)

else :
    print("Enter valid choice")