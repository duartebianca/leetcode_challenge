class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # criar dicionario vazio
        vistos = {}
        for i in range(len(nums)):
            if nums[i] in vistos:
                return True
            vistos[nums[i]] = i
        return False

# --- Para seu teste local (opcional) ---
sol = Solution()
print(f"Teste 1 (Esperado: True): {sol.containsDuplicate([1, 2, 3, 1])}")
print(f"Teste 2 (Esperado: False): {sol.containsDuplicate([1, 2, 3, 4])}")
print(f"Teste 3 (Esperado: True): {sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])}")
print(f"Teste 4 (Esperado: False): {sol.containsDuplicate([])}")