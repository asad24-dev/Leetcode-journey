from collections import Counter
import heapq
def reorganizeString(s):
        wordDict = Counter(s)
        maxkey = max(wordDict, key = wordDict.get)
        maxval = wordDict[maxkey]
        remchars = len(s) - maxval
        if maxval > remchars + 1:
            return ""
        heap = [(-freq, char) for char, freq in wordDict.items()]
        heapq.heapify(heap)
        result = []
        prevchar = ''
        prevcount = 0
        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)

            if prevcount < 0:
                heapq.heappush(heap, (prevcount, prevchar))

            prevchar, prevcount = char, count + 1
        result = ''.join(result)  
        for i in range(1, len(result)):
            if result[i] == result[i - 1]:
                return ""
        return result

print(reorganizeString("vvvlo"))