def groupAnagrams(strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

'''The code groups anagrams using a defaultdict with list as the default 
factory, ensuring that each key starts with an empty list. For each 
string, a count list of size 26 tracks the frequency of each letter 
(ord(c) - ord('a') maps characters to indices). The tuple(count) creates 
an immutable, hashable key representing the character composition of the 
string. This key groups anagrams in the dictionary, and the string is 
appended to the corresponding list. Finally, list(res.values()) returns 
all grouped anagrams as a list of lists.'''