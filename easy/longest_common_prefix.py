class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # lista vazia
        if not strs:
            return ""

        prefix = ""
        
        #  itera por cada caracter da primeira palavra
        for i in range(len(strs[0])):     
            # Pega o caractere da coluna atual
            char_referencia = strs[0][i] 
            # itera por todas as palavras na lista
            for palavra in strs:
                # se a palavra é mais curta que o índice ou se é diferente do caracter de referencia
                if ( (len(palavra) < i+1 ) or (palavra[i] != char_referencia) ):
                    # retornamos o que já tem
                    return prefix 
            
            # Se o loop de dentro terminou sem problemas, significa que todas tem char_referencia
            prefix += char_referencia
            
        return prefix
