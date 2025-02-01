def calPoints(coperations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ret = []
        for i in range(len(operations)):
            if operations[i] == 'D':
                ret.append(ret[-1] * 2)
            elif operations[i] == 'C':
                ret.pop()
            elif operations[i] == '+':
                ret.append(ret[-1] + ret[-2])
            else:
                ret.append(int(operations[i]))
        sum = 0
        for i in ret:
            sum += i
        return sum