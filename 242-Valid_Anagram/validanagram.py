def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) != len(s):
            return False
        if (Counter(s) - Counter(t)) == {}:
            return True
        else:
            return False
'''Counter is a dictionary subclass which helps to count the number of elements in a list
string = "hello world"
# Use Counter
result = Counter(string)
print(result)
Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
so if the difference of the counter of s and t is an empty dictionary then that means it is an anagram'''
