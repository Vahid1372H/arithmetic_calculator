from iostream import get_float_number
from operations import get_operator


def get_operator():
    operators = {"-", "+", "*", "/", "//", "**","%"}
    user_operator= input("Enter your operator: ")
    if not user_operator in operators :
        return False
    return user_operator


def get_float_number(prompt: str) -> float:
    user_input = input(prompt)
    if user_input is float:
        return user_input
    raise ValueError


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
    result = (number_1, number_2, user_operator,user_operators)
    print(result)


if __name__ == "__main__":
    main()