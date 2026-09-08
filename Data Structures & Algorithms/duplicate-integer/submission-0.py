class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        
        # hashmap, i is the index and num is the value
        for i, num in enumerate(nums):
            
            # state what a duplicate is 
            duplicate = num
            if duplicate in seen:
                return True
            seen[num] = i # this loads the value in the dict if not a dupl
        return False

        