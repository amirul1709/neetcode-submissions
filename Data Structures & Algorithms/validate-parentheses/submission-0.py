class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}' : '{', ']' : '[', ')' : '('}

        for par in s:
            if par in closeToOpen:
                if stack and stack[-1] == closeToOpen[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)

        if stack:
            return False
            
        return True