# Last updated: 1/8/2026, 5:25:00 p.m.
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        options = []

        for i in range(2, 10):
            number = deque(digits[:i])
            options.append(int(''.join(number)))

            for j in range(i, 9):
                number.popleft()
                number.append(digits[j])
                options.append(int(''.join(number)))

        ans = []
        for op in options:
            if low <= op <= high: ans.append(op)

        return ans