from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    ages = list(age_dict.values())  # state what ages is (its the value in the dict)

    return ages  # then print those ages



# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
