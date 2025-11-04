from validation import is_operator


def get_operator(prompt: str = "Enter an operator: ") -> str:
    if not prompt.isalnum() or not prompt.isalpha():
        return True
    return False


    # if not isinstance(prompt, str):
    #     raise TypeError("The prompt argument type should be 'str'.")

while True:
    prompt = input(prompt)
    if is_operator(prompt):
        print(prompt)
    else:
        print(f"Error: {prompt} is invalid.")