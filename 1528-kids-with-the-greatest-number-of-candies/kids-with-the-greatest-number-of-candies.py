class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        extra_cand = extraCandies
        candies = candies
        
        bool_array = []

        for i in candies:
            if int(i) + extra_cand >= max(candies):
                bool_array.append(True)
            else:
                bool_array.append(False)
        return bool_array
        