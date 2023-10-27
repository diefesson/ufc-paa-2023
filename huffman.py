from bisect import insort
from typing import List


class No:
    def __init__(self, valor: str or None, freq: int, filhos: List["No"]):
        self.valor = valor
        self.freq = freq
        self.filhos = filhos


def huffman(valores: List[str], frequencias: List[int], aridade: int) -> No:
    nos = []
    for v, f in zip(valores, frequencias):
        insort(nos, No(v, f, []), key=lambda n: n.freq)
    while len(nos) > 1:
        quantidade = min(len(nos), aridade)
        filhos = [nos.pop(0) for _ in range(quantidade)]
        filhos = list(reversed(filhos))
        freq = sum(map(lambda n: n.freq, filhos))
        no = No(None, freq, filhos)
        insort(nos, no, key=lambda n: n.freq)
    return nos[0]


def imprimir_huffman(raiz: No):
    codigo = []
    _imprimir_huffman(raiz, codigo)


def _imprimir_huffman(no: No, codigo: List[int]):
    if no.valor is not None:
        print(codigo, no.valor, no.freq)
        return
    for i, f in enumerate(no.filhos):
        codigo.append(i)
        _imprimir_huffman(f, codigo)
        codigo.pop(-1)


if __name__ == "__main__":
    valores = ["a", "b", "c", "d", "f"]
    frequencias = [45, 13, 12, 16, 9, 5]
    aridade = 3
    raiz = huffman(valores, frequencias, aridade)
    imprimir_huffman(raiz)
