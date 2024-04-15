


class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if char.isalnum()  == True:
                string += char.lower()
        print(string)
        return string == string[::-1]
