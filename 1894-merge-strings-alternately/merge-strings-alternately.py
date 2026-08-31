class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = word1
        w2 = word2
        l,r = 0,0
        merge_str = []
        while l < len(w1) and r < len(w2):
            merge_str.append(w1[l])
            merge_str.append(w2[r])
            l += 1
            r += 1

        merge_str.extend(w1[l:])
        merge_str.extend(w2[r:])
        return "".join(merge_str)