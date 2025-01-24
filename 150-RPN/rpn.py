def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)):
            operation = tokens[i]
            if operation == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif operation == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)  # Correct order: a - b
            elif operation == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif operation == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22