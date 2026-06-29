class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]
        
        for bracket in s:
            match stack[-1]:
                case "(":
                    if bracket == ")":
                        stack.pop()
                    else:
                        stack.append(bracket)
                case "[":
                    if bracket == "]":
                        stack.pop()
                    else:
                        stack.append(bracket)
                case "{":
                    if bracket == "}":
                        stack.pop()
                    else:
                        stack.append(bracket)
                case 0:
                    stack.append(bracket)
        return True if stack[-1] == 0 else False