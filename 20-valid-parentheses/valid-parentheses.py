class Solution:
    def isValid(self, s: str) -> bool:
        p={")":"(","]":"[","}":"{"}
        stack=[]

        for i in s:
            if i in p:
                if not stack or stack[-1]!=p[i]:
                    return False
                stack.pop()
                
            else:
                stack.append(i)
        
        return len(stack)==0