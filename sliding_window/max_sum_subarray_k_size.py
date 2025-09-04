from typing import List


def find_max_sum_subarray(my_list: List[int], k: int) -> int:
    length = len(my_list)
    i = 0
    j = 0
    total = 0
    max_sum = float('-inf')

    while j < length:
        total += my_list[j]

        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if total > max_sum:
                max_sum = total
            total -= my_list[i]
            i += 1
            j += 1

    return max_sum


my_list = [2, 3, 5, 2, 9, 7, 1]
k = 3
print(find_max_sum_subarray(my_list=my_list, k=k))
