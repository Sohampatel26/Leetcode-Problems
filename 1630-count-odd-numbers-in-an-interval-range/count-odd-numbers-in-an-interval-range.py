class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff=high-low+1
        if low%2!=0 and high%2!=0 :
            return (diff//2)+1
        return diff//2