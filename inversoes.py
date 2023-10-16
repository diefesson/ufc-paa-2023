from typing import List


def inversoes_simples(arr: List[int]) -> int:
    n = len(arr)
    inversoes = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversoes += 1
    return inversoes


if __name__ == "__main__":
    arr = [3, 6, 4, 9, 10, 1, 5, 7, 8, 2]
    inversoes = inversoes_simples(arr)
    print(f"array: {arr}")
    print(f"inversoes: {inversoes}")
