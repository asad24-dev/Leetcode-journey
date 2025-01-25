
def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    stack = []
    retarr = []
    flag = False
    for i in range(len(temperatures)):
        if i == len(temperatures) - 1:
            retarr.append(0)
        else:
            count = i + 1
            stack.append(temperatures[i])
            while not flag and count <= len(temperatures) - 1:
                if temperatures[count] > stack[0]:
                    flag = True
                else:
                    stack.append(temperatures[count])
                    count +=  1
            if flag:
                retarr.append(len(stack))
                stack = []
                flag = False
            else:
                retarr.append(0)
    return retarr
            
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])) # [1, 1, 4, 2, 1, 1, 0, 0]
        