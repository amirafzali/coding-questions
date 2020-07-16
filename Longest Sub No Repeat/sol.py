class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1: return len(s)
        
        lookup = {}
        start = longest = 0
        
        for i in range(len(s)):
            char = s[i]
            
            if char in lookup and lookup[char] >= start:
                start = lookup[char]+1
            
            lookup[char] = i
            
            longest = max(longest, i-start+1)
        
        return longest