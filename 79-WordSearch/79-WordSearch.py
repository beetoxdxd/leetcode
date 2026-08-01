# Last updated: 1/8/2026, 5:27:57 p.m.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        boardLetterCounts = Counter(ch for row in board for ch in row)
        requiredCounts = Counter(word)

        if any(boardLetterCounts[ch] < requiredCounts[ch] for ch in word):
            return False
        
        if boardLetterCounts[word[0]] > boardLetterCounts[word[-1]]:
            word = word[::-1]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < R and 0 <= j < C
        
        offsets = [(-1,0), (1,0), (0,-1), (0, 1)]
        def dfs(i: int, j: int, d: int) -> bool:
            # base case
            if d == len(word) - 1:
                return True

            # mark this node as seen (#)
            # we don't need to save the original letter because we know it must be word[d]
            board[i][j] = '#'

            # recursive cases
            # visit all neighbors as long as:
            #   the index is in bounds
            #   we have not seen it before
            #   the target letter is correct
            candidates = [(i+offsetX, j+offsetY) for (offsetX,offsetY) in offsets if in_bounds(i+offsetX, j+offsetY)]
            #print(f"candidates for {i}, {j} are {candidates}")
            #print(f"word = {word} and word[d={d}] = {word[d]}")
            
            for candidateX, candidateY in candidates:
                if board[candidateX][candidateY] == word[d+1]:
                    if dfs(candidateX, candidateY, d+1):
                        return True
            # post recursion, unmark this node as seen
            board[i][j] = word[d]
            
            return False
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False