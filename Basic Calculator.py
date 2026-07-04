import math 
print("1.Find Addition")
print("2.Find Subtraction")
print("3.Find Multiply")
print("4.Division")
print("5.Remainder")
print("6.Logarithm")
print("7.Square Root")
print("8.Exponantial")
print("9.LCM")
print("10.HCF")
print("11.Percentage")
print("12.Value of SIN")
print("13.Value of COS")
print("14.Power ")

choice = int(input("Enter your choice "))

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

if choice == 1 :
    print("Addition ",num1 + num2)

elif choice == 2 :
    print("Subtraction ",num1 - num2)

elif choice == 3 :
    print("Multiplication ",num1 * num2)

elif choice == 4 :
    if num2 == 0:
        print("Division is not possible")
    else :
        print("Divide",num1 / num2)

elif choice== 5 : 
    print("Remainder ",num1 % num2)

elif choice == 6 :
    if num1 <= 0 :
        print("Enter positive value of num1")
    else :
        print("log of first number ",math.log10(num1))
    if num2 <= 0 :
        print("Enter positive value of num2")
    else :
        print("log of second number ",math.log10(num2))

elif choice == 7 :
    if num1 < 0 :
        print("Enter non negative value of num1")
    else :
        print("square root of first number",math.sqrt(num1))
    if num2 < 0 :
        print("Enter non negative value of num2")
    else :
        print("square root of secong number",math.sqrt(num2))

elif choice == 8 :
    print("exponantial of first number",math.exp(num1))
    print("exponantial of second number",math.exp(num2))

elif choice== 9 :
    print("LCM of both number ",math.lcm(num1 ,num2))

elif choice == 10 :
    print("HCF of both number ",math.gcd(num1 , num2))

elif choice == 11 :
    total = int(input("Enter total number"))
    print("Percentage of first number ", float(num1  / total * 100 ))
    print("Percentage of second number ", float(num2 / total * 100 ))

elif choice == 12 :
    print("value of sin for first number is ",math.sin(math.radians(num1)))
    print("value of sin for second number is ",math.sin(num2))

elif choice == 13 :
    print("value of cos for first number is ",math.cos(num1))
    print("value of cos for second number is ",math.cos(num2))

elif choice == 14 :
    print("Power of first number with respect to second number is ",pow(num1 , num2))

else :
    print("Invalid choice")