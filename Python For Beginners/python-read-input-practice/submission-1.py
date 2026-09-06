def add_two_numbers() -> int:
    user_input = input() # take input
    string_list = user_input.split(",") # split the number input by commas
    # the numbers are still strings rn

    return int(string_list[0]) + int(string_list[1])
    # turn each string into an int and then add them up


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
