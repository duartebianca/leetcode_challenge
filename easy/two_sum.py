class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # criar dicionário vazio
        vistos = {}
        # laço para checar os elementos
        for i in range(len(nums)):
            # checar num[i]
            if (target - nums[i]) in vistos:
                return [vistos[target - nums[i]], i]
            else:
                vistos[nums[i]] = i
