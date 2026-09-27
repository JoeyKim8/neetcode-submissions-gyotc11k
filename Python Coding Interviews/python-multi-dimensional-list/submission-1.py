from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    end_list = [] # initiate the resulting list
    for sublist in nested_arr: # loop thru nested array
        max_in_sublist = sublist[0] # initiate finding max element in sublist
        for element in sublist: # loop thru sublist
            max_in_sublist = max(max_in_sublist, element) # find the max element
        end_list.append(max_in_sublist) # add the max element to the resulting list
    return end_list

# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
