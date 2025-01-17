class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack=[]

        l= len(temperatures)
        count=[0]*l

        for i in range(l):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                k=stack.pop()
                count[k]=i-k
            stack.append(i)

        return count
