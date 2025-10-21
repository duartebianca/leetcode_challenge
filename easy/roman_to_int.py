class Solution:
    def romanToInt(self, s: str) -> int:
        em_numero = 0
        symbols_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50, 
            "C": 100,
            "D": 500,
            "M": 1000
        }
        valor_anterior = 0
        for c in s[::-1]:
            valor_atual = symbols_map[c]
            # Se o valor atual é menor que o anterior, subtrai
            if valor_atual < valor_anterior:
                em_numero -= valor_atual
            else: # Senão (se for maior ou igual), soma
                em_numero += valor_atual
            # Atualiza o valor anterior para a próxima iteração
            valor_anterior = valor_atual
            
        return em_numero  
