# Last updated: 22/7/2026, 5:56:33 p.m.
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0: return []
        
        # 1. Prefix Max: El valor más alto desde el inicio hasta i
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
            
        # 2. Suffix Min: El valor más bajo desde i hasta el final
        suffix_min = [0] * n
        suffix_min[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])
            
        # 3. Procesar bloques
        ans = [0] * n
        start = 0
        
        for i in range(n):
            # Verificamos si i es el final de un bloque de conectividad
            if i == n - 1 or prefix_max[i] <= suffix_min[i+1]:
                # El máximo alcanzable en este bloque es el pico más alto
                block_max = prefix_max[i]
                for k in range(start, i + 1):
                    ans[k] = block_max
                
                start = i + 1
                
        return ans