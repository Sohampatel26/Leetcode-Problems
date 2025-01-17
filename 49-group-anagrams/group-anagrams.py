class Solution(object):
    def groupAnagrams(self, strs):
        sol=defaultdict(list)
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            sol[tuple(count)].append(i)
        return sol.values()

