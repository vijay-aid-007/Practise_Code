class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')' :'(',
            '}' : '{',
            ']' : '['
        }

        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif stack == []:
                return False
            elif stack[-1] != mapping[i]:
                return False    
            else:
                stack.pop()
        return stack == []
    
            