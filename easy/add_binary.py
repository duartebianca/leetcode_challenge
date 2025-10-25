class Solution:
    def addBinary(self, a: str, b: str) -> str:
        size_max = max(len(a), len(b))
        soma = ""
        carry = 0

        # iguala os tamanhos com zeros a esquerda
        a = a.zfill(size_max)
        b = b.zfill(size_max)

        for i in range(size_max - 1, -1, -1):
            soma_numerica = int(a[i]) + int(b[i]) + carry

            # bit atual do resultado
            bit = soma_numerica % 2
            soma = str(bit) + soma

            # define o carry pro próximo loop
            carry = soma_numerica // 2

        # se sobrou carry no final, adiciona no início
        if carry:
            soma = "1" + soma

        return soma
