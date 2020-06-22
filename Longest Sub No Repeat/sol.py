class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1: return len(s)

        window = {}
        start = longest = 0

        for i,char in enumerate(s):
            if char in window and window[char] >= start:
                start = window[char]+1
            window[char] = i
            longest = max(longest, i-start)
        
        return longest+1