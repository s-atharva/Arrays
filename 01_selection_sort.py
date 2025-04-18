from typing import List


# Time Complexity = O(n^2)

def selection_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        mini_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini_index]:
                mini_index = j
        temp = arr[mini_index]
        arr[mini_index] = arr[i]
        arr[i] = temp
    return arr


my_arr: List[int] = [64, 25, 12, 22, 11]
sorted_arr: List[int] = selection_sort(arr=my_arr)
print("Sorted Array", sorted_arr)
