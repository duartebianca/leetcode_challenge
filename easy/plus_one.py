class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Pega o tamanho da lista
        n = len(digits)
        for i in range(n - 1, -1, -1):
            
            # Tenta somar 1 no dígito atual
            digits[i] += 1
            # Verifica se não estourou
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
        return [1] + digits
