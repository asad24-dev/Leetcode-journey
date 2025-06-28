class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        triedict = self.trie
        for c in word:
            if c not in triedict:
                triedict[c] = {}
            triedict = triedict[c]
        triedict['end'] = 'end'

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        triedict = self.trie
        for c in word:
            if c not in triedict:
                return False
            triedict = triedict[c]
        return 'end' in triedict

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        triedict = self.trie
        for c in prefix:
            if c not in triedict:
                return False
            triedict = triedict[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)