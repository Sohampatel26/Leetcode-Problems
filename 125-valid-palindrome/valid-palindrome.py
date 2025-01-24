class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        ll=len(s)//2       
        for i in range(ll):
            if s[i]!=s[len(s)-i-1]:
                return False
        return True