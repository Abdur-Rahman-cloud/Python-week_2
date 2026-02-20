#  Part A: Loops

### Q1. Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)

### Q2. Print even numbers from 2 to 20 using a for loop.
for i in range(2, 21, 2):
    print(i)

### Q3. Print all characters of the string "Python" using a loop.
for ch in "Python":
    print(ch)

### Q4. Print numbers from 5 to 1 using a loop.
for i in range(5, 0, -1):
    print(i)

### Q5. Use a while loop to print numbers from 1 to 5.
i = 1
while i <= 5:
    print(i)
    i += 1

#  Part B: Functions

### Q6. Create a function that prints "Hello Python" when called.
def greet():
    print("Hello Python")
    greet()

### Q7. Create a function that takes one number and prints it.
def print_number(num):
    print(num)
    print_number(10)

### Q8. Create a function that takes two numbers and prints their sum.
def add_numbers(a, b):
    print(a + b)

add_numbers(5, 7)

### Q9. Create a function that takes one number and checks whether it is even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(4)

### Q10. Create a function that prints numbers from 1 to 5 using a loop.
def print_numbers():
    for i in range(1, 6):
        print(i)

print_numbers()


#  Mini Project: Number Table Generator
### Create a function that prints the multiplication table of a number (1 to 10)
def number_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

number_table(3)


