class Solution:
    def reverse(self, x: int) -> int:
        if x>2**31 or x<(-2)**31:
            return 0
        
        s=str(abs(x))

        if int(s[::-1])>2**31:
            return 0
        if x>=0:
            return int(s[::-1])
        else:
            return (-1)*int(s[::-1])