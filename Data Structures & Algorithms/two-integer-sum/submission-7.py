class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # initiate a dict to keep track of each number and its indices
        for i, num in enumerate(nums): # enumerate(nums) takes your list and gives you both the index and the value, num is the actual value and i=index

            # check for the complement first
            complement = target - num 
            if complement in seen:
                return [seen[complement], i]
            # if the complement is not found, remember this number for later
            # basically stores it in the seen dictionary (key=num, value=i)
            seen[num] = i

        