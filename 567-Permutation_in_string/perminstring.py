def checkInclusion(s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1arr = [0] * 26
        s2arr = [0] * 26
        for i in range(len(s1)):
            s1arr[ord(s1[i]) - ord('a')] += 1
            s2arr[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            if s1arr[i] == s2arr[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2arr[index] += 1
            if s1arr[index] == s2arr[index]:
                matches += 1
            elif s1arr[index] + 1 == s2arr[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2arr[index] -= 1
            if s1arr[index] == s2arr[index]:
                matches += 1
            elif s1arr[index] - 1 == s2arr[index]:
                matches -= 1

            l += 1

        return matches == 26