def hanoi(numero_discos: int):
    _hanoi(numero_discos, 1, 3, 2)


def _hanoi(
    n: int, origem: int, destino: int, auxiliar: int
):
    if n == 0:
        return
    _hanoi(n - 1, origem, auxiliar, destino)
    print(f'{origem} -> {destino}')
    _hanoi(n - 1, auxiliar, destino, origem)


if __name__ == "__main__":
    numero_discos = 4
    hanoi(numero_discos)
