def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard")


greet("Najmus", "Saqib")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Bill")
print(message)

# by default a function returns None
print(greet("John", "Doe"))


def increment(number, by):
    return number + by


print(increment(2, 1))

# by here is a keyword argument
print(increment(2, by=2))


# example of an optional parameter
# optional parameter has to come after required parameter
# no required parameter can come after the optional paramter
# def decrement(nummber, by=1, another) is wrong and will throw an error
def decrement(number, by=1):
    return number - by


print(decrement(4))


# xargs
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4))


# xxargs
def save_user(**user):
    print(user)


save_user(id=1, name="John", age=22)


# scope
def greet(name):
    message = "a"


# name and message variable are different in these two functions
# they only exists inside these functions and cannot be accessed from outside
def send_email(name):
    message = "b"


message = "global"


def greet(name):
    message = "local"  # not changing the global message variable


greet("asa")

print(message)


def greet(name):
    global message
    message = "local"  # will change but working the global variable and changing them in fn is a bad practice


greet("sas")
print(message)


# Excercise
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"

    return input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
