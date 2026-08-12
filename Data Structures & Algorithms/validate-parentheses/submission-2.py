class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        close_to_open = {")" : "(", "}" : "{", "]" : "["}

        for p in s:
            if p in close_to_open:
                if stack and stack[-1] == close_to_open[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        if not stack:
            return True
        else:
            return False