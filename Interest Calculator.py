# Simple Interest Calculator

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (years): "))

# enter simple interest or compound interest

c = input("Enter the type of interest do you want to find")
if c in ["simple interest" , "Simple interst" ,"Simple Interest"] :

    si = (principal * rate * time) / 100

    print("Simple Interest =", si)
    print("Total Amount =", principal + si)

elif c in ["compound interest" , "Compound interest" , "Compound Interest"] : 

    amount = principal * (1 + rate / 100) ** time
    ci = amount - principal

    print("Compound Interest =", round(ci, 2))
    print("Total Amount =", round(amount, 2))

else :
    print("Enter a valid type")