class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        total = [0 for _ in range(26)];
        for char in s:
            total[ord(char)-ord('a')]+=1
        for char in t:
            total[ord(char)-ord('a')]-=1
        for index in range(26):
            if total[index]:
                return False
        return True