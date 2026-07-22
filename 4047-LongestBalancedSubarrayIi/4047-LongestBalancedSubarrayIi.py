# Last updated: 22/7/2026, 5:56:24 p.m.
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree_min = [0] * (4 * n)
        self.tree_max = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _push(self, v):
        if self.lazy[v] != 0:
            for child in [2 * v, 2 * v + 1]:
                self.tree_min[child] += self.lazy[v]
                self.tree_max[child] += self.lazy[v]
                self.lazy[child] += self.lazy[v]
            self.lazy[v] = 0

    def update(self, v, tl, tr, l, r, add):
        if l > r: return
        if l == tl and r == tr:
            self.tree_min[v] += add
            self.tree_max[v] += add
            self.lazy[v] += add
        else:
            self._push(v)
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm), add)
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add)
            self.tree_min[v] = min(self.tree_min[2 * v], self.tree_min[2 * v + 1])
            self.tree_max[v] = max(self.tree_max[2 * v], self.tree_max[2 * v + 1])

    def find_rightmost_zero(self, v, tl, tr, l, r):
        # Si el 0 no está en el rango de valores de este nodo, fuera.
        if l > r or not (self.tree_min[v] <= 0 <= self.tree_max[v]):
            return -1
        if tl == tr:
            return tl
        
        self._push(v)
        tm = (tl + tr) // 2
        # Intentamos primero por la derecha para maximizar el largo
        res = self.find_rightmost_zero(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
        if res == -1:
            res = self.find_rightmost_zero(2 * v, tl, tm, l, min(r, tm))
        return res

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        next_occ = {}
        next_pos = [n] * n
        # Mapeamos la siguiente aparición de cada número
        for i in range(n - 1, -1, -1):
            if nums[i] in next_occ:
                next_pos[i] = next_occ[nums[i]]
            next_occ[nums[i]] = i
        
        st = SegmentTree(n)
        ans = 0
        
        # Barrido de derecha a izquierda
        for i in range(n - 1, -1, -1):
            val = 1 if nums[i] % 2 == 0 else -1
            # nums[i] solo afecta el balance hasta que vuelve a aparecer
            st.update(1, 0, n - 1, i, next_pos[i] - 1, val)
            
            # Buscamos el j más lejano donde el balance sea 0
            j = st.find_rightmost_zero(1, 0, n - 1, i, n - 1)
            if j != -1:
                ans = max(ans, j - i + 1)
                
        return ans