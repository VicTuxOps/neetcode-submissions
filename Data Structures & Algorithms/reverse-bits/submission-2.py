class Solution:
    def reverseBits(self, n: int) -> int:
        i = 32
        out = 0
        while i > 0:
            out = out << 1
            if (n & 1):
                out += 1
            n = n >> 1
            i-=1
        print(bin(out))
        return out