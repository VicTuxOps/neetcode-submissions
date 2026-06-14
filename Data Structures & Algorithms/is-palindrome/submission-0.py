class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(char for char in s if char.isalnum()).lower()
        l, r = 0, len(new)-1
        while l < r:
            if new[l] != new[r]:
                return False
            l+=1
            r-=1
        return True