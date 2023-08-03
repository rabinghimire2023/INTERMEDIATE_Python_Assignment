"""Given an array of strings (str), group the anagrams together. You can return the
answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once."""

from collections import defaultdict

def group_anagrams(strs):
    grouped_anagrams = defaultdict(list)
    for s in strs:
        sorted_str = ''.join(sorted(s))
        grouped_anagrams[sorted_str].append(s)
    
    return list(grouped_anagrams.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result) #output:[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]