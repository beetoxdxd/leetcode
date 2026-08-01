# Last updated: 1/8/2026, 5:26:52 p.m.
class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        actual = ""
        cont = 0
        i = 0

        while i < length:
            if chars[i] == actual:
                cont += 1
                chars.pop(i)
                length -= 1
            else:
                if cont > 1:
                    cont_str = str(cont)
                    for j in cont_str:
                        chars.insert(i, j)
                        i += 1
                        length += 1
                actual = chars[i]
                cont = 1
                i += 1

        if cont > 1:
            cont_str = str(cont)
            for j in cont_str:
                chars.insert(i, j)
                i += 1
        return len(chars)