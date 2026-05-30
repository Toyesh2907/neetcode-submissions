import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = s.translate(
            str.maketrans('', '', string.punctuation)
        )
        cleaned_string = cleaned_string.lower()
        cleaned_string = cleaned_string.replace(" ", "")
        print(cleaned_string)

        print(cleaned_string[::-1])
        return cleaned_string == cleaned_string[::-1]