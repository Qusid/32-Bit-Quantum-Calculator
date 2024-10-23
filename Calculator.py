from Upto32BitAdder import Adder
from Upto32BitMultiplier import Multiply
from Upto32Subtractor import Sub

# This function adds two numbers
def add(x, y):
    return Adder(x,y)

# This function subtracts two numbers
def subtract(x, y):
    return Sub(x,y)

# This function multiplies two numbers
def multiply(x, y):
    return Multiply(x,y)



print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(int(num1), int(num2)))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(int(num2), int(num1)))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(int(num1), int(num2)))
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
        
