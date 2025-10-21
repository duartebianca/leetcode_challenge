class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicio_s = {}
        dicio_t = {}
        for i in range(len(s)):
            if s[i] in dicio_s:
                dicio_s[s[i]] += 1
            else:
                dicio_s[s[i]] = 1
            if t[i] in dicio_t:
                dicio_t[t[i]] += 1
            else:
                dicio_t[t[i]] = 1
        # compara os dois dicionarios
        return dicio_s == dicio_t



# --- Para seu teste local (opcional) ---
sol = Solution()
print(f"Teste 1 (Esperado: True): {sol.isAnagram('anagrama', 'nagarama')}")
print(f"Teste 2 (Esperado: False): {sol.isAnagram('rato', 'carro')}")
print(f"Teste 3 (Esperado: False): {sol.isAnagram('a', 'ab')}")
print(f"Teste 4 (Esperado: False): {sol.isAnagram('aacc', 'ccac')}")