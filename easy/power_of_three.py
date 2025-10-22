from math import log, pow, floor
class Solution:
    # solução com loops
    def isPowerOfThree(self, n: int) -> bool:
        potencia_atual = 1
        if n <=0:
            return False
        while (potencia_atual <= n):
            if (potencia_atual == n):
                return True
            else:
                potencia_atual *= 3
        return False
    # solução sem loops
    def isPowerOfThree_without_loops(self, n: int) -> bool:
      # considere x como o expoente da maior potencia de 3 possível no intervalo
      # temos um numero 3**x <= 2**31 - 1
      # ou seja, x = log₃(2**31 - 1)
      expoente_max_potencia = floor(log( (pow(2, 31)-1), 3))
      MAX_POTENCIA_DE_3 = pow (3, expoente_max_potencia)
      potencia_atual = 1
      if n <=0:
        return False
      return MAX_POTENCIA_DE_3 % n == 0
