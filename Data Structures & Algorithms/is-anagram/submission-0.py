from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionaryS = defaultdict(int) # initiate a dict, every key starts with value=int
        dictionaryT = defaultdict(int)

        for char in s:
            dictionaryS[char] += 1
        for char in t:
            dictionaryT[char] += 1
        if dictionaryS == dictionaryT:
            return True
        else:
            return False
        

        