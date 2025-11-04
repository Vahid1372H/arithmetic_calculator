from validation import is_operator


def get_operator(operator: str = "Enter an operator: ") -> str:
    operators = {"-", "+", "*", "/", "//", "**","%"}
    if not operator in operators :
        return False
    return True


while True:
    prompt = input(prompt)
    if is_operator(prompt):
        print(prompt)
    else:
        print(f"Error: {prompt} is invalid.")