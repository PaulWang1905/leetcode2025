class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        if s == ' ':
            return True
        def getChar(i,direction):
            if i < 0 or i >= len(s):
                return i
            if s[i].isalnum():
                return i
            else:
                if direction == 0:  # move right
                    return getChar(i + 1, 0)
                elif direction == 1:  # move left
                    return getChar(i - 1, 1)
        l = 0
        r = len(s) -1

        while l < r:  
            l = getChar(l, 0)
            r = getChar(r, 1)  
            if l >= r:
                break        
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

