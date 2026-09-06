from typing import List

def read_integers() -> List[int]:
    user_input = input()
    string_list = user_input.split(",") # split the input by the commas
    list_of_int = [] # initiate a list

    for string in string_list: # go thru every string in string_list
        list_of_int.append(int(string)) # turn each string into an integer by using int(), add it to the list by APPENDING it
    
    return list_of_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
