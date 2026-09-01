class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        # BRUTE FORCE
        # result = []

        # for i in range(len(s)-k+1):
        #     window_size = s[i:i+k]
        #     length = len([i for i in window_size if i in 'aeiou'])
        #     result.append(length)
        
        # return max(result)
        vowels = 'aeiou'
        count = sum(1 for ch in s[:k] if ch in vowels)
        max_count = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1 
            if s[i-k] in vowels:
                count -= 1 
            max_count = max(max_count, count)
        return max_count




