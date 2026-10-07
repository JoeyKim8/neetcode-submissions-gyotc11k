class Solution:
    def isValid(self, s: str) -> bool:
        # "Most recent first" is LIFO and thats a stack

        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        
        return s == ''
        