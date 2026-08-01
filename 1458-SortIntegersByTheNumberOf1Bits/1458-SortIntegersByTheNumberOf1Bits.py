# Last updated: 1/8/2026, 5:24:13 p.m.
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def counting(num: int) -> int:
            return (bin(num).count('1'), num)

        arr.sort(key=counting)
        return arr