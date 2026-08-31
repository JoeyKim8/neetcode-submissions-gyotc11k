from typing import List

def count_unique_words(words: List[str]) -> int:
    words_set = set(words) # to change the list into a set
    return len(words_set) # just simply return how many items are now in the set

    if "hello" in words == True:
        return False

    return 0

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
