# Last updated: 1/8/2026, 5:28:46 p.m.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n-1

        while i <= j:
            h = (i+j)//2

            if nums[h] == target:
                i, j = 0, h-1
                start = h
                while i <= j:
                    aux = (i+j)//2
                    if nums[aux] == target:
                        start = aux
                        j = aux-1
                    elif nums[aux] < target: i = aux+1
                    else: break

                end = h
                i, j = h+1, n-1
                while i <= j:
                    aux = (i+j)//2
                    if nums[aux] == target:
                        end = aux
                        i = aux+1
                    elif nums[aux] > target: j = aux-1
                    else: break

                return [start, end]
            elif nums[h] > target: j = h-1
            else: i = h+1

        return [-1,-1]