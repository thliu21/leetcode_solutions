"""
sliding window
"""

def charToInt(ch):
    return ord(ch)-ord('a')

class Solution:
    def check(contained, required):
        for i in range(26):
            if contained[i] != required[i]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        required = [0 for _ in range(26)]
        contained = [0 for _ in range(26)]
        for i in range(len(s1)):
            required[charToInt(s1[i])] += 1
            contained[charToInt(s2[i])] += 1
        if self.check(contained, required):
            return True
        for i in range(1, len(s2)-len(s1)+1):
            contained[charToInt(s2[i-1])] -= 1
            contained[charToInt(s2[i+len(s1)-1])] += 1
            if self.check(contained, required):
                return True
        return False
