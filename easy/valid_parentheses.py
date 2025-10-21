class Solution:
    def isValid(self, s: str) -> bool:
        minha_pilha = []
        if len(s) == 1:
            return False
        for i in range(len(s)):
            if not minha_pilha or s[i] in ['(', '[', '{']:
                minha_pilha.append(s[i])
            else:
                topo = minha_pilha.pop()
                if (topo == "{") and (s[i] == "}"):
                    pass
                elif (topo == "[") and (s[i] == "]"):
                    pass
                elif (topo == "(") and (s[i] == ")"):
                    pass
                else:
                    return False
        return len(minha_pilha) == 0


            

# --- Para seu teste local (opcional) ---
sol = Solution()
print(f"Teste 1 (Esperado: True): {sol.isValid('()')}")
print(f"Teste 2 (Esperado: True): {sol.isValid('()[]{}')}")
print(f"Teste 3 (Esperado: False): {sol.isValid('(]')}")
print(f"Teste 4 (Esperado: False): {sol.isValid('([)]')}")
print(f"Teste 5 (Esperado: True): {sol.isValid('{[]}')}")
print(f"Teste 6 (Esperado: False): {sol.isValid('[')}")
print(f"Teste 7 (Esperado: False): {sol.isValid(']')}")
print(f"Teste 8 (Esperado: False): {sol.isValid('()[')}")