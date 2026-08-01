# Last updated: 1/8/2026, 5:28:24 p.m.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            h = [0] * 26
            for char in s:
                h[ord(char) - ord("a")] += 1
            ans[tuple(h)].append(s)

        return list(ans.values())