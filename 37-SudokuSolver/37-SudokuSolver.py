# Last updated: 1/8/2026, 5:28:40 p.m.
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Usamos arreglos de enteros (0 por defecto, ningún bit encendido)
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9
        empty_cells = set()

        # Mascara completa para los números 1-9 (bits del 1 al 9 encendidos)
        # Binario: 1111111110 (510 + 2 = 512, pero usamos bits 1-9)
        FULL_MASK = 0x3FE 

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.add((r, c))
                else:
                    val = int(board[r][c])
                    mask = 1 << val
                    rows[r] |= mask
                    cols[c] |= mask
                    squares[(r // 3) * 3 + (c // 3)] |= mask

        def get_options_mask(r, c):
            # Combinamos las restricciones con OR y luego invertimos con XOR
            used = rows[r] | cols[c] | squares[(r // 3) * 3 + (c // 3)]
            return FULL_MASK & ~used

        def traverse() -> bool:
            if not empty_cells:
                return True

            # --- HEURÍSTICA MRV con BITS ---
            min_options = 10
            best_cell = None
            best_mask = 0

            for r, c in empty_cells:
                options_mask = get_options_mask(r, c)
                count = options_mask.bit_count() # Cuenta cuántos 1s hay
                
                if count == 0: return False
                if count < min_options:
                    min_options = count
                    best_cell = (r, c)
                    best_mask = options_mask
                    if count == 1: break

            r, c = best_cell
            idx_s = (r // 3) * 3 + (c // 3)
            empty_cells.remove((r, c))

            # Iterar sobre los bits encendidos en la máscara
            for num in range(1, 10):
                if (best_mask >> num) & 1:
                    mask = 1 << num
                    # Aplicar movimiento
                    board[r][c] = str(num)
                    rows[r] |= mask
                    cols[c] |= mask
                    squares[idx_s] |= mask

                    if traverse(): return True

                    # Backtrack (usamos XOR para apagar el bit)
                    rows[r] ^= mask
                    cols[c] ^= mask
                    squares[idx_s] ^= mask

            board[r][c] = "."
            empty_cells.add((r, c))
            return False

        traverse()