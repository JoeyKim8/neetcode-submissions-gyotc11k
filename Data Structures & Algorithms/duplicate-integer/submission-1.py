class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # we would use a set instead of a hashmap since we dont need to key each value
        
        # hashmap, i is the index and num is the value
        for i, num in enumerate(nums):
            
            # state what a duplicate is 
            duplicate = num
            if duplicate in seen:
                return True
            seen.add(num) # this loads the value in the set if not a dupl
        return False

        