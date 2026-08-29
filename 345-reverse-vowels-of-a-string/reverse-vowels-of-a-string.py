class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        string_list = list(s)
        left, right = 0, len(s)-1


        while left < right:
            if string_list[left] not in vowels:
                left += 1
            elif string_list[right] not in vowels:
                right -= 1
            else:
                string_list[left], string_list[right] = string_list[right], string_list[left]
                left += 1
                right -= 1
            
        return "".join(string_list)
        