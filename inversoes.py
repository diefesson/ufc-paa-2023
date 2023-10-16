from typing import List, Tuple


def inversions_simple(arr: List[int]) -> int:
    n = len(arr)
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions


def inversions_ms(arr: List[int]) -> int:
    inversions, _ = _inversion_ms(arr)
    return inversions


def _inversion_ms(arr: List[int]) -> Tuple[List[int], int]:
    if len(arr) <= 1:
        return 0, arr.copy()
    else:
        middle = len(arr) // 2
        left_inv, left_arr = _inversion_ms(arr[:middle])
        right_inv, right_arr = _inversion_ms(arr[middle:])
        merge_inv, sorted = _merge(left_arr, right_arr)
        inversions = left_inv + right_inv + merge_inv
    return inversions, sorted


def _merge(left_arr: List[int], right_arr: List[int]) -> Tuple[List[int], int]:
    sorted = []
    inversions = 0
    i = 0
    j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            sorted.append(left_arr[i])
            i += 1
        else:
            inversions += len(left_arr) - i
            sorted.append(right_arr[j])
            j += 1
    while i < len(left_arr):
        sorted.append(left_arr[i])
        i += 1
    while j < len(right_arr):
        sorted.append(right_arr[j])
        j += 1
    return inversions, sorted


if __name__ == "__main__":
    arr = [3, 6, 4, 9, 10, 1, 5, 7, 8, 2]
    simple_count = inversions_simple(arr)
    ms_count = inversions_ms(arr)
    print(f"array: {arr}")
    print(f"simple count: {simple_count}")
    print(f"ms count: {ms_count}")
