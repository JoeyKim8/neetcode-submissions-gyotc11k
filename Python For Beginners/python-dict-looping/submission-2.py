from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    result = []  # we want to take the names and put it in a list
    for key in age_dict:
        result.append(key)  # adds each name/key to the list
    return result

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    result = []  # create an empty list again
    for key in age_dict:
        value = age_dict[key]  # state what a value is
        result.append(value)
    return result

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
