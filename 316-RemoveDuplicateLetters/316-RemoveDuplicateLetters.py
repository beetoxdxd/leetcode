# Last updated: 1/8/2026, 5:27:06 p.m.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        h = defaultdict(int)

        for char in s:
            h[char] += 1

        ans = []
        for i in range(len(s)):
            h[s[i]] -= 1
            if s[i] in ans: continue
                
            while ans and ord(s[i]) <= ord(ans[-1]) and h[ans[-1]]: ans.pop()
            ans.append(s[i])

        return ''.join(ans)