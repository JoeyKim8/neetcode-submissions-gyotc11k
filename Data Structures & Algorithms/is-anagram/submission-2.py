from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # set initial parameters
    
        dictionaryS = defaultdict(int) # initiate a dict, every key starts with value=int
        dictionaryT = defaultdict(int) # create 2 dicts

        for char in s:
            dictionaryS[char] += 1 # update the count for each char in s
        for char in t:
            dictionaryT[char] += 1 # update the count for each char in t
        if dictionaryS == dictionaryT: # if they have the same counts then True
            return True
        else:
            return False
        

        