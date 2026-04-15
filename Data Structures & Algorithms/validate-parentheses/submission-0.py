class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validParen = {")":"(",
        "]":"[", "}":"{"}

        for c in s:
            if c in validParen:
                if stack and stack[-1] == validParen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False