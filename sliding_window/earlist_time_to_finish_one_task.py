from typing import List


def earliest_time(tasks: List[List[int]]) -> int:
    earliest_finish_time = float("inf")  # store the minimum finishing time

    for start_time, duration in tasks:  # meaningful names
        finish_time = start_time + duration
        if finish_time < earliest_finish_time:
            earliest_finish_time = finish_time

    return earliest_finish_time


print(earliest_time(tasks=[[1, 6], [2, 3]]))
