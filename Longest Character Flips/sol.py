def characterReplacement(self, s, k):
    if not s: return 0
    
    longest = max_freq = 0
    i = 0
    freq = {char:0 for char in s}
    
    for j in range(len(s)):
        freq[s[j]]+=1
        max_freq = max(max_freq, freq[s[j]])
        while j-i+1-max_freq > k:
            freq[s[i]]-=1
            i+=1
        longest = max(longest, j-i+1)
        
    return longest