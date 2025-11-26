class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        tam = len(arr)
        for i in range(tam):
            if tam == 2:
                return True
            # a diferenca será sempre
            diferenca = arr[0] - arr[1]
            if (i+1) < tam:
                if arr[i] - arr[i+1] == diferenca:
                    resposta = True
                else:
                    return False
        return resposta

        
