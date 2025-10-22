# O comando awk processa um arquivo linha por linha
awk '
# o bloco executa para cada linha do bloco de entrada
{
    # NF = (Número de Campos/Colunas) na linha atual.
    for (i = 1; i <= NF; i++) {
        if (a[i] == "") {
            a[i] = $(i)
        } else {
            a[i] = a[i] " " $(i)
        }
    }
}

# O bloco "END" é uma regra especial do awk.
# Ele só é executado UMA VEZ, depois que TODAS as linhas do arquivo foram lidas.
END {

    for (j = 1; j <= NF; j++) {
        
        # Imprime o conteúdo de cada elemento do array em uma nova linha.
        print a[j]
    }
}
' file.txt
