from iostream import get_float_number
from operations import get_operator


def get_operator():
    operators = {"-", "+", "*", "/", "//", "**","%"}
    user_operator= input("Enter your operator: ")
    if not user_operator in operators :
        return False
    return user_operator


def get_float_number():
    user1 = input("Enter your float_number1: ")
    user2 = input("Enter your float_number2: ")
    if user1.isalpha() or user2.isalpha():
        return False 
    return user1,user2


def addition(a,b):
    return a + b

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
    number_1 = get_float_number()
    number_2 = get_float_number()
    user_operator = get_operator()
    user_operators = {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division,
        "//": division_floor,
        "%": modulus,
        "**": power,
    }
    result = addition(number_1, number_2, user_operator,user_operators)
    print(result)


if __name__ == "__main__":
    main()