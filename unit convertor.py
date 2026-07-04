print("1.Meter to Kilometer")
print("2. Kilometer to Meter")
print("3. Centimeter to Meter")
print("4. Meter to Centimeter")
print("5. Centimeter to Millimeter")
print("6. Meter to Millimeter")
print("7. Millimeter to Centimeter")
print("8. Millimeter to meter")

choice = int(input("Enter your choice : "))

value = float(input("Enter value: "))

if choice == 1:
    print("Result = ",value / 1000, "km")

elif choice == 2:
    print("Result = ",value * 1000, "m")

elif choice == 3:
    print("Result = ",value / 100, "m")

elif choice == 4:
    print("Result = ",value * 100, "cm")

elif choice == 5:
    print("Result = ",value * 10, "mm")

elif choice == 6:
    print("Result = ",value *1000, "mm")

elif choice == 7:
    print("Result = ",value / 10, "cm")

elif choice == 8:
    print("Result = ",value / 1000, "m")

else:
    print("Invalid Choice")