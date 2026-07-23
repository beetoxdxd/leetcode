# Last updated: 22/7/2026, 11:36:16 p.m.
from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # 1. Contamos las frecuencias a velocidad de C. 
        # Esto reduce nuestro espacio de trabajo a máximo 676 elementos.
        word_counts = Counter(words)
        
        pal_length = 0
        has_central_pivot = False

        # 2. Iteramos SOLO sobre las palabras únicas
        for word, count in word_counts.items():
            # Caso A: Palabras con letras iguales (ej. "aa", "bb")
            if word[0] == word[1]:
                # Formamos parejas de "aa" con "aa"
                pal_length += (count // 2) * 4
                # If queda una suelta, puede ir en el centro del palíndromo
                if count % 2 == 1:
                    has_central_pivot = True
            
            # Caso B: Palabras con letras distintas (ej. "ab")
            # Usamos 'word < word[::-1]' para procesar "ab" y "ba" una sola vez
            elif word < word[::-1]:
                rev = word[::-1]
                if rev in word_counts:
                    # Las parejas posibles son el mínimo entre ambas frecuencias
                    pairs = min(count, word_counts[rev])
                    pal_length += pairs * 4

        # 3. Si encontramos al menos una palabra tipo "aa" suelta, 
        # la ponemos en el centro (+2 de longitud)
        if has_central_pivot:
            pal_length += 2

        return pal_length