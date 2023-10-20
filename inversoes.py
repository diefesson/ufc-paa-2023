from typing import List, Tuple


def inversoes_simples(arr: List[int]) -> int:
    n = len(arr)
    inversoes = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversoes += 1
    return inversoes


def inversoes_ms(arr: List[int]) -> int:
    inversoes, _ = _inversoes_ms(arr)
    return inversoes


def _inversoes_ms(arr: List[int]) -> Tuple[List[int], int]:
    if len(arr) <= 1:
        return 0, arr.copy()
    else:
        meio = len(arr) // 2
        inv_esq, arr_esq = _inversoes_ms(arr[:meio])
        inv_dir, arr_dir = _inversoes_ms(arr[meio:])
        inv_merge, ordenado = _merge(arr_esq, arr_dir)
        inversoes = inv_esq + inv_dir + inv_merge
    return inversoes, ordenado


def _merge(arr_esq: List[int], arr_dir: List[int]) -> Tuple[List[int], int]:
    ordenado = []
    inversoes = 0
    i = 0
    j = 0
    while i < len(arr_esq) and j < len(arr_dir):
        if arr_esq[i] <= arr_dir[j]:
            ordenado.append(arr_esq[i])
            i += 1
        else:
            inversoes += len(arr_esq) - i
            ordenado.append(arr_dir[j])
            j += 1
    while i < len(arr_esq):
        ordenado.append(arr_esq[i])
        i += 1
    while j < len(arr_dir):
        ordenado.append(arr_dir[j])
        j += 1
    return inversoes, ordenado


if __name__ == "__main__":
    arr = [3, 6, 4, 9, 10, 1, 5, 7, 8, 2]
    simple_count = inversoes_simples(arr)
    ms_count = inversoes_ms(arr)
    print(f"array: {arr}")
    print(f"contagem simples: {simple_count}")
    print(f"contagem ms: {ms_count}")
