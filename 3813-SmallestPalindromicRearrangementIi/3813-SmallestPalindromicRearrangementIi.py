# Last updated: 1/8/2026, 5:19:46 p.m.
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        def mult_coef(n: int, k_list: List[int]):
            res = 1
            actual_n = n

            for elem in k_list:
                res *= math.comb(actual_n, elem)
                actual_n -= elem
            return res

        h = [0] * 26

        for char in s:
            h[ord(char) - 97] += 1

        n = 0
        odd = -1
        for i in range(26):
            if h[i] % 2: odd = i
            h[i] //= 2
            n += h[i]

        p = mult_coef(n, h)
        if k > p: return ''

        ans = []
        for i in range(n):
            for j in range(26):
                if h[j] == 0: continue

                pos = (p * h[j]) // (n-i)
                if k <= pos: 
                    ans.append(chr(j + 97))
                    h[j] -= 1
                    p = pos
                    break
                else:
                    k -= pos

        first_half = ''.join(ans)
        center = chr(odd + 97) if odd != -1 else ''

        return first_half + center + first_half[::-1]