from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    dictionary = defaultdict(int) # initiate a dict, every key starts with value=int

    for char in s: # loop thru each letter in the string
        dictionary[char] += 1 # this adds the count of each char to the dict
    return dictionary


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    dictionary = defaultdict(list)

    for sublist in nums: # loop thru each element (sublist) in the list
        first = sublist[0] # set the key as the first element in the sublist
        for i in range(1, len(sublist)): # loop thru sublist starting from 2nd element
            dictionary[first].append(sublist[i]) # add rest of elements from sublist to the value part of the dictionary
    
    return dictionary


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
