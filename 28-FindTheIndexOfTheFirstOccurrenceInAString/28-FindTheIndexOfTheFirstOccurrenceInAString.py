# Last updated: 1/8/2026, 5:28:56 p.m.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def constructLps(pat, lps):
            len_ = 0
            m = len(pat)
            lps[0] = 0

            i = 1
            while i < m:
                if pat[i] == pat[len_]:
                    len_ += 1
                    lps[i] = len_
                    i += 1
                else:
                    if len_ != 0: len_ = lps[len_ - 1]
                    else:
                        lps[i] = 0
                        i += 1

        n, m = len(haystack), len(needle)
        lps = [0] * m
        constructLps(needle, lps)
        i, j = 0, 0

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == m: return i - j
            else:
                if j != 0: j = lps[j - 1]
                else: i += 1
        return -1