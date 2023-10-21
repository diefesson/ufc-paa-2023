from typing import List, Tuple


def viagem(hoteis: List[int]) -> Tuple[List[int], List[int]]:
    n = len(hoteis)
    paradas_anteriores = [-1] * n
    reclamacoes = [-1] * n
    reclamacoes[0] = (200 - hoteis[0]) ** 2
    for i in range(1,n):
        mpa = -1
        mr = (200 - hoteis[i]) ** 2
        for j in range(i):
            r = reclamacoes[j] + (200 - (hoteis[i] - hoteis[j])) ** 2
            if r < mr:
                mpa = j
                mr = r
        paradas_anteriores[i] = mpa
        reclamacoes[i] = mr
    return paradas_anteriores, reclamacoes

def print_viagem(hoteis, paradas_anteriores, reclamacoes):
    _print_viagem(hoteis, paradas_anteriores, reclamacoes, len(hoteis)-1)

def _print_viagem(hoteis, paradas_anteriores, reclamacoes, h):
    anterior = paradas_anteriores[h]
    if anterior != -1:
        _print_viagem(hoteis, paradas_anteriores, reclamacoes, anterior)
    print(f"hotel {h} no km {hoteis[h]} com {reclamacoes[h]} reclamacoes")

if __name__ == '__main__':
    hoteis = [180, 200, 219, 380, 400]
    print('hoteis', hoteis)
    paradas_anteriores, reclamacoes = viagem(hoteis)
    print_viagem(hoteis, paradas_anteriores, reclamacoes)
