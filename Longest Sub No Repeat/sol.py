class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1: return len(s)
        found = {}
        start = 0
        longest = 1
        
        for i,char in enumerate(s):
            if char in found and found[char] >= start:
                start = found[char]+1
            found[char] = i
                
            longest = max(longest, i-start+1)
            
        return longest