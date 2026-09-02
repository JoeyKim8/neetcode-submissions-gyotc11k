from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count = {}
    for char in word:  # first loop thru everything in each word
        if char not in count:
            count[char] = 0 # to prevent KeyError
        count[char] += 1 # when this specific char comes up, it will get incremented by 1
    return count




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
