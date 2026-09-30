from typing import List, Dict


def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    my_hashmap = {} # initiate the hash map

    for i, j in zip(keys, values): # loop thru both lists using zip()
        my_hashmap[i] = j # i = keys and j = values
    return my_hashmap


def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    my_list = []

    for key in keys:
        value = hash_map[key] # set what a value is
        my_list.append(value) # add the value of the keys in [keys] inside the list
    return my_list



# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))
