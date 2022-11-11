# This was my first Algorithm problem and passes all test cases but is slow

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        count = 0
        longest = 0
        k = 0
        i = k
        res = []
        
        for j in range(0, len(s)):
            while i < len(s):
                if s[i] not in res:
                    res.append(s[i])
                    count += 1
                    if count > longest:
                        longest = count
                    i += 1
                else:
                    res.clear()
                    count = 0
                    k += 1
                    i = k
        
        return longest