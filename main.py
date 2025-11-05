from iostream import get_float_number
from operations import get_operator


def get_operator():
    user_operator= input("Enter your operator: ")
    operators = {"-", "+", "*", "/", "//", "**","%"}
    if not user_operator in operators :
        return False
    return True


def get_float_number():
    user1 = input("Enter your float_number1: ")
    user2 = input("Enter your float_number2: ")
    if user1.isalpha() or user2.isalpha():
        return False 
    return True


def addition():
    number_1 = input("Enter your num1: ")
    number_2 = input("Enter your num2: ")
    s = number_1 + number_2
    print(s)
print(get_float_number())
print(get_operator("+"))

def subtraction():
    pass


def multiplication():
    pass


def division():
    pass


def division_floor():
    pass


def modulus():
    pass


def power():
    pass






def main():
    number_1 = input("Enter your num1: ")
    number_2 = input("Enter your num2: ")
    user_operator= input("Enter your operator: ")
    s = number_1 + number_2
    print(s)
    print(user_operator)


if __name__ == "__main__":
    main()