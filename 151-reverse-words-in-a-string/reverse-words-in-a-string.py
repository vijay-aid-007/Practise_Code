class Solution:
    def reverseWords(self, s: str) -> str:
        words  = s.strip()
        words1 = words.split()
        list_1  = list(words1)
        
        l,r = 0, len(list_1)-1

        while l < r:
            list_1[l], list_1[r] = list_1[r], list_1[l]
            l += 1 
            r -= 1 
        return " ".join(list_1)
        