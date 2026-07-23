# Last updated: 22/7/2026, 11:36:21 p.m.
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1: return encodedText
        decoded = []
        n = len(encodedText)
        columns = n // rows

        for i in range(columns):
            r, pos = 0, i

            while r < rows and pos < columns:
                decoded.append(encodedText[r * columns + pos])
                pos += 1
                r += 1

        return ''.join(decoded).rstrip()