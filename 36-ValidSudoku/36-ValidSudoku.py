# Last updated: 1/8/2026, 5:28:42 p.m.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Usamos sets para búsquedas O(1)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # Calcular el índice del cuadrado (0-8)
                s_idx = (r // 3) * 3 + (c // 3)
                
                # Verificar duplicados
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[s_idx]):
                    return False
                
                # Agregar a los registros
                rows[r].add(val)
                cols[c].add(val)
                squares[s_idx].add(val)

        return True