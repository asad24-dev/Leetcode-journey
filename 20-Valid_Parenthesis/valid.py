def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dicttest = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in dicttest:
                if stack and stack[-1] == dicttest[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
    
print(isValid("()")) # True
