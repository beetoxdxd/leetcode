# Last updated: 1/8/2026, 5:23:53 p.m.
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        index_aux = 0
        size = len(target)
        for i in range(1, n+1):
            stack.append("Push")
            if i == target[index_aux]: index_aux += 1
            else: stack.append("Pop")

            if index_aux == size: return stack

        return stack