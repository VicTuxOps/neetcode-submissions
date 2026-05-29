class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""

        for s in strs:
            out += str(len(s)) + "#" + s

        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]

            out.append(word)

            i = j + 1 + length

        return out