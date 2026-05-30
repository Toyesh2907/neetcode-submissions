class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        secret = "_my_secret_"
        for string in  strs:
            encoded_string = encoded_string + string + secret
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        secret = "_my_secret_"
        current_string = ""
        for character in s:
            current_string += character
            if secret in current_string:
                decoded_list.append(current_string.replace(secret, ""))
                current_string = ""
        print(decoded_list)
        return decoded_list