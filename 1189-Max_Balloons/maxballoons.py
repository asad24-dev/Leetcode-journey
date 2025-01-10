def maxNumberOfBalloons(text):
        """
        :type text: str
        :rtype: int
        """
        maindict = Counter(text)
        b_freq, a_freq, l_freq, o_freq, n_freq = 0, 0, 0, 0, 0
        if 'b' in maindict:
            b_freq = maindict['b']
        if 'a' in maindict:
            a_freq = maindict['a']
        if 'l' in maindict:
            l_freq = maindict['l']
        if 'o' in maindict:
            o_freq = maindict['o']
        if 'n' in maindict:
            n_freq = maindict['n']
        words = min(l_freq, o_freq)
        words = int(words / 2)
        return min(b_freq, a_freq, n_freq, words)