# comparison operator
print("bag" > "apple")  # true bcz if we sort them bag comes after apple
print("10" == 10)
print(ord("a"))

# if else statement
temperature = 20
if temperature > 30:
    print("it's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

# ternary operator
age = 22
message = "ELigible" if age >= 18 else "Not eligibe"
print(message)

# logical operator
high_income = False
good_credit = True
student = True
if high_income and good_credit:
    print("High income and Good credit")
else:
    print("High income or Good credit")

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

if not student:
    print("ELigible")
else:
    print("Not eligible")

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# Chaining comparison operator
age = 22
if age >= 18 and age < 65:
    print("Eligible")
if 18 <= age < 65:  # Preferred way to do
    print("Eligible")


# loops
for number in range(1, 4):
    print("Attempt", number, number * ".")

# for else loop
success = False
for number in range(1, 4):
    print("Attempt", number, number * ".")
    if success:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Iterable
print(type(range(1)))

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)


# While loop
number = 10
while number > 0:
    print(number)
    number -= 1

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

while True:
    command2 = input(">")
    print("ECHO", command2)
    if command.lower() == "quit":
        break

# quiz
number_of_even_number = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        number_of_even_number += 1
else:
    print(f"We have {number_of_even_number} even numbers")
