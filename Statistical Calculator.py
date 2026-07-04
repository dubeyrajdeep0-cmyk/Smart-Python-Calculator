import statistics
import math
numbers = list(map(float, input("Enter numbers separated by space: ").split()))

print("Numbers entered :", numbers)
print("1. Sum")
print("2. Mean")
print("3. Median")
print("4. Mode")
print("5. Variance")
print("6. Standard Deviation")

choice = int(input("Enter your choice"))
if choice == 1:
    print("sum of all the data",sum(numbers))
    
elif choice == 2 :
    print("mean of given number is ",statistics.mean(numbers))

elif choice == 3:
    print("median of the given numbers is ",statistics.median(numbers))

elif choice == 4:
    print("Mode of the given numbers is ",statistics.mode(numbers))

elif choice == 5:
    print("Varience of the given numbers is ",statistics.variance(numbers))

elif choice == 6:
    print("Standard Deviation of given numbers is ",statistics.stdev(numbers))

else :
    print("Invlid choice")