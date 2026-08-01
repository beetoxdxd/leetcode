# Last updated: 1/8/2026, 5:24:55 p.m.
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        max_sum = [[0] * (n+1) for _ in range(n+1)]
        number_paths = [[0] * (n+1) for _ in range(n+1)]
        directions = [(0,1), (1,0), (1,1)]
        mod = 10**9 + 7

        max_sum[n-1][n-1] = 0
        number_paths[n-1][n-1] = 1

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X' or board[i][j] == 'S': continue
                if board[i][j] == 'E': aux = 0
                else: aux = int(board[i][j])

                max_current = max(max_sum[i+1][j], max_sum[i][j+1], max_sum[i+1][j+1])

                for dx, dy in directions:
                    if max_current != max_sum[i+dx][j+dy]: continue
                    number_paths[i][j] = (number_paths[i][j] + number_paths[i+dx][j+dy]) % mod

                if number_paths[i][j] > 0: max_sum[i][j] = max_current + aux
                else: max_sum[i][j] = 0

        return [max_sum[0][0], number_paths[0][0]]