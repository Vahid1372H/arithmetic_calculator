def get_operator(prompt: str = "Enter an operator: ") -> str:
    if not isinstance(prompt, str):
        raise TypeError("The prompt argument type should be 'str'.")

    while True:
        number = input(prompt)
        if is_float(number):
            return float(number)
        else:
            print(f"Error: {number} is invalid.")