w = float(input("Enter your body weight in kg "))
h = float(input("Enter your height in m "))
BMI = w / h**2
print("Your BMI is : ",BMI)
if BMI < 18.5 :
    print("You are Under weight")

elif BMI < 25 :
    print("You are Normal weight")

elif BMI < 30 :
    print("You are Over weight")

else :
    print("You are Obese")