class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # initiate group for containing each sublist
        # how this could look:
        # groups = {
        # "act":  ["act", "cat"],
        # "opst": ["pots", "tops", "stop"],
        # "aht":  ["hat"]
        # }

        # loop thru list
        for word in strs:
            key = "".join(sorted(word)) # turn list into a string so it can be a key
            # word = "act"   ->  key = "act"
            # word = "pots"  ->  key = "opst"
            if key in groups: # if key is already in groups, add word to existing list
                groups[key].append(word)
            # if key not in groups, make a new list with the word in it
            else:
                groups[key] = [word] # make sure to put [] to make it a list
            
        return list(groups.values())
        # u want to only return the values(), which are the lists
        # u want to wrap this all in a complete list
                
            

        