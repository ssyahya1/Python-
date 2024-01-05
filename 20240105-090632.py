# Prompt the user to enter two floating-point numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the average
average = (num1 + num2) / 2

# Display the result with two decimal places
print(f"The average of {num1:.2f} and {num2:.2f} is {average:.2f}")