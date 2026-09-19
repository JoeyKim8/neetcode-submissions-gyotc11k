from typing import List


def disallow_negatives(num: int) -> int:
    return max(0, num) # returns either 0 or num (if num >= 0)


def max_difference(nums: List[int]) -> int:
    output = 0 # intialize the value

    for i in range(len(nums) - 1): # loop thru the list 
        output = max(output, nums[i+1] - nums[i]) # after max it starts with "output," because we set the value of "output" as the minimum value. so basically if "nums[i+1] - num[i]" is more than the current "output" value then we update the "ouput" value to be that value.
    return output



# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
