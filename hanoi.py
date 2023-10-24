from typing import List, Tuple


def hanoi(numero_discos: int) -> List[Tuple[int, int]]:
    movimentos = []
    _hanoi(numero_discos, 1, 3, 2, movimentos)
    return movimentos


def _hanoi(
    n: int, origem: int, destino: int, auxiliar: int, movimentos: List[Tuple[int, int]]
):
    if n == 0:
        return
    _hanoi(n - 1, origem, auxiliar, destino, movimentos)
    movimentos.append((origem, destino))
    _hanoi(n - 1, auxiliar, destino, origem, movimentos)


def imprimir_movimentos(movimentos: List[Tuple[int, int]]):
    digitos_movimentos = len(str(len(movimentos)))
    mascara_movimentos = f"0{digitos_movimentos}d"
    for i, (ori, dest) in enumerate(movimentos):
        print(f"{i:{mascara_movimentos}}. {ori} -> {dest}")


if __name__ == "__main__":
    numero_discos = 4
    movimentos = hanoi(numero_discos)
    imprimir_movimentos(movimentos)
