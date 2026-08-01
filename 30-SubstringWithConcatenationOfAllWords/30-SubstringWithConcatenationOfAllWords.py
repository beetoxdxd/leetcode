# Last updated: 1/8/2026, 5:28:54 p.m.
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        h = defaultdict(int)
        for word in words:
            h[word] += 1
        
        i = 0
        l = len(words[0])
        n = len(s)
        m = len(words)
        window = m*l
        ans = []

        for i in range(l):
            left, right = i, l+i
            aux = defaultdict(int)
            cont = 0

            while right <= n:
                word = s[right-l:right]

                if word in h:
                    aux[word] += 1
                    cont += 1

                    while aux[word] > h[word]:
                        l_word = s[left:left+l]
                        aux[l_word] -= 1
                        cont -= 1
                        left += l
                    
                    if cont == m:
                        ans.append(left)
                else:
                    cont = 0
                    aux.clear()
                    left = right

                right += l

        return ans