# Last updated: 1/8/2026, 5:23:05 p.m.
class Solution:
    def interpret(self, command: str) -> str:
        aux = []
        ans = []

        for char in command:
            if char == 'G': ans.append(char)
            elif aux and char == ')':
                if aux[-1] == '(': ans.append('o')
                else: ans.append('al')
                
                aux = []
            else: aux.append(char)

        return ''.join(ans)