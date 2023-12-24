class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        n = len(s)
        result = 0
        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
        return result

#Time Complexity - O(n)



