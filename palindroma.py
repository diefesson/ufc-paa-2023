from typing import Tuple


def palindroma(sequencia: str) -> Tuple[int, int]:
    n = len(sequencia)
    ini = 0
    fim = 1
    palindromas = [[ False for j in range(n+1)] for i in range(n)]
    for i in range(n):
        palindromas[i][i+1] = True
    for i in range(n-1):
        if sequencia[i] == sequencia[i + 1]:
            palindromas[i][i + 2] = True
            ini = i
            fim = i + 2
    for tam in range(3,n+1):
        for i in range(n-tam):
            f = i + tam
            if sequencia[i] == sequencia[f-1] and palindromas[i+1][f-1]:
                palindromas[i][f] = True
                ini = i
                fim = f
    return ini, fim

if __name__ == '__main__':
    sequencia = 'abccdceecf'
    print(sequencia)
    ini, fim = palindroma(sequencia)
    print(f'de {ini} até {fim} temos {sequencia[ini:fim]}')
