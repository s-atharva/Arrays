from typing import List


def find_max_sum_subarray(arr: List[int], window_size: int) -> List[int]:
    start = 0
    end = 0
    n = len(arr)
    output = []
    sum = 0
    while end < n:
        sum += arr[end]
        if end - start + 1 < window_size:
            end += 1
        else:
            output.append(sum)
            sum -= arr[start]
            start += 1
            end += 1
    return output


my_list: List[int] = [1, 2, 3, 4, 5, 6]
k = 3
print(find_max_sum_subarray(arr=my_list, window_size=k))
