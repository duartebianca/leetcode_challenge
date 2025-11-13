# primeira solucao

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        vistos = []
        duplicados = []
        single = 0
        for i in range(len(nums)):
            if nums[i] in vistos:
                duplicados.append(nums[i])
            else:
                vistos.append(nums[i])
        return list(set(vistos) - set(duplicados))[0]


# segunda solucao
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_ordenada = sorted(nums)
        single = 0
        tam = len(nums)
        if tam == 1:
            return nums_ordenada[0]
        for i in range(0, tam - 1, 2):
            if nums_ordenada[i] != nums_ordenada[i+1]:
                return nums_ordenada[i]
        return nums_ordenada[tam-1] 
