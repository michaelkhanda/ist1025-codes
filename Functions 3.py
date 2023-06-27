def validateInputs(prompt, lower, upper):
    """Validates inputs"""
    while True:
        number = int(input(prompt))
        if number <lower or number > upper:
            print("Error:the number must be between "+\
                  str(lower) + "and" + str(upper))
        else:
            return number
