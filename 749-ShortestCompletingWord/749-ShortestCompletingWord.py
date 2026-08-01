# Last updated: 1/8/2026, 5:26:02 p.m.
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        ans = 'aaaaaaaaaaaaaaa'
        word = licensePlate.lower()
        h = [0]*26

        for char in word:
            if ord(char) >= ord('a') and ord(char) <= ord('z'): h[ord(char) - ord('a')] += 1

        for word in words:
            aux = h[:]

            for char in word:
                if aux[ord(char) - ord('a')] > 0: aux[ord(char) - ord('a')] -= 1

            flag = True
            for i in range(26):
                if aux[i] != 0: flag = False

            if flag and len(word) < len(ans): ans = word

        return ans
