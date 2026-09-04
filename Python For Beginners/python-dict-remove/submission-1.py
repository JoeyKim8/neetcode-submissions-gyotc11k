from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    for k in keys:  # iterate over every key in the list of keys
        my_dict.pop(k, 0) # check that the key exists in my_dict, if not return 0
    return my_dict




# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))
