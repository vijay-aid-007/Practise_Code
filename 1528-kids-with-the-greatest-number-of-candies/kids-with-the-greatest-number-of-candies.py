class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        list_1 = candies
        maximum = max(candies)
        extra_candies = extraCandies

        result = []
        for i in list_1:
            new_val = i+extra_candies
            if new_val >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result