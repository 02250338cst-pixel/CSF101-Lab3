# Program to check if a number is positive, negative, or zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Program to check if a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even")
else:
   print("The number is odd")

# Program to find the largest of two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is larger")
else:
    print(f"{num2} is larger")
# Program to find the largest of three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3
print(f"{largest} is the largest number")

# Program to display grade based on marks
marks = float(input("Enter marks: "))

if marks >= 80:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print(f"Grade {grade}")

# Menu-driven program for basic arithmetic operations
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    result = num1 + num2
    print(f"Sum = {result}")
elif choice == 2:
    result = num1 - num2
    print(f"Difference = {result}")
elif choice == 3:
    result = num1 * num2
    print(f"Product = {result}")
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"Quotient = {result}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid choice")


part B : Loops (for and while)
# Program to print numbers from 1 to 10
for i in range(1, 11):
    print(i, end=" ")
8. Print all even numbers from 1 to 20

# Program to print even numbers from 1 to 20
for i in range(2, 21, 2):
    print(i, end=" ")
9. Sum of the first 10 natural numbers

# Program to find sum of first 10 natural numbers
sum_total = 0
for i in range(1, 11):
    sum_total += i
print(f"Sum = {sum_total}")
10. Multiplication table of a given number

# Program to display multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
11. Print numbers from 1 to 5 using a while loop

# Program to print numbers 1 to 5 using while loop
i = 1
while i <= 5:
    print(i, end="")
    i += 1
12. Sum from 1 to n using a while loop

# Program to calculate sum from 1 to n
n = int(input("Enter n: "))
sum_total = 0
i = 1
while i <= n:
    sum_total += i
    i += 1
print(f"Sum = {sum_total}")
13. Keep taking input until the user enters 0

# Program to keep taking input until 0
while True:
    num = int(input("Enter number: "))
    if num == 0:
        print("Loop ended")
        break


Part C: Break and Continue
14. Print numbers 1 to 10 but stop at 6 using break
for i in range(1, 11):
    if i == 6:
        break
    print(i, end="")
15. Print numbers 1 to 10 but skip 5 using continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end="")
16. Search for a number in a list and stop when found

# Program to search for a number in a list
numbers = [2, 4, 6, 8, 10]
search = int(input("Searching for: "))

for num in numbers:
    if num == search:
        print("Number found")
        break


Part D: Functions
# Function that prints “Hello, World!”
def hello():
    print("Hello, World!")

hello()

#Function that returns the square of a number
def square(n):
    return n * n

num = int(input("Enter number: "))
print(f"Square = {square(num)}")

# Function to add two numbers
def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Sum = {add(num1, num2)}")

# Function to check even or odd
def even_odd(n):
    if n % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

num = int(input("Enter number: "))
even_odd(num)

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = int(input("Enter number: "))
print(f"Factorial = {factorial(num)}")

# Function to print multiplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

num = int(input("Enter number: "))
multiplication_table(num)
Part E: Integrated Programs

# Numbers from 1 to n and display even/odd
def even_odd(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(f"{i} -> Even")
        else:
            print(f"{i} -> Odd")

n = int(input("Enter n: "))
even_odd(n)

# Menu-driven calculator using functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 5:
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print(f"Sum = {add(num1, num2)}")
    elif choice == 2:
        print(f"Difference = {subtract(num1, num2)}")
    elif choice == 3:
        print(f"Product = {multiply(num1, num2)}")
    elif choice == 4:
        print(f"Quotient = {divide(num1, num2)}")
    else:
        print("Invalid choice")
