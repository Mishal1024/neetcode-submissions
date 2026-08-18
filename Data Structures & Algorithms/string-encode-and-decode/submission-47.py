class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string = encoded_string + f"{len(string)}#{string}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        length = ""
        out = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                length = str(length) + s[i]
            elif s[i] == "#":
                string = ""
                length = int(length)
                while length != 0 and i < len(s)-1:
                    i += 1
                    length -= 1
                    string = string + s[i]
                out.append(str(string))
            i += 1
        return out