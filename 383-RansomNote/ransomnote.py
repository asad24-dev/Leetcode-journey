def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if Counter(ransomNote) - Counter(magazine) == {}:
            return True
        else:
            return False
            
            
'''Counter is a dictionary subclass which helps to count the number of elements in a list
string = "hello world"
# Use Counter
result = Counter(string)
print(result)
Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
so if the difference of the counter of the ransomNote and magazine is an empty dictionary then that means it is a subset of magazine'''
