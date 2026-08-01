# Last updated: 1/8/2026, 5:29:18 p.m.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = math.inf
        answer = 0

        for i in range(n):
            left = i+1
            right = n-1
            inner = target-nums[i]

            while left < right:
                suma = nums[left] + nums[right]
                aux = abs(inner-suma)
                if aux < ans:
                    answer = suma + nums[i]
                    ans = aux
                if suma < inner: left += 1
                else: right -= 1

            
        return answer