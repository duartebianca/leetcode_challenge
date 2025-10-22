# primeira solução: lenta, usa busca linear
from math import floor
class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0
        while (True):
            if ((result * result == x) or ((result+1) * (result+1) > x)):
                return floor(result)
            else:
                result +=1
    # segunda solução: busca binária
    def mySqrt_2(self, x: int) -> int:
        # Casos base
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        # Define os limites da nossa busca
        esquerda = 1
        direita = x
        melhor_resposta = 0
        
        while esquerda <= direita:
            meio = (esquerda + direita) // 2            
            if meio * meio == x:
                # Se acharmos a raiz exata, retornamos na hora
                return meio
            
            if quadrado < x:
                melhor_resposta = meio
                esquerda = meio + 1
            else:
                direita = meio - 1
        return melhor_resposta
