my_dict = {
    'a': 1,
    'b': 1,
    'c': 1
}


def find_longest_substr_unique_char(my_str: str) -> int:
    i = 0
    j = 0
    max_unique = 0
    my_dict = dict()
    n = len(my_str)
    while j < n:
        if my_str[j] in my_dict:
            my_dict[my_str[j]] += 1
        else:
            my_dict[my_str] = 1

            if len(my_dict) < j - i + 1:
                j += 1

            if len(my_dict) == j - i + 1:
                max_unique = max(max_unique, j - i + 1)


print(len(my_dict))
total = 0
for item in my_dict:
    total += my_dict[item]
print(total)
print(len(my_dict) == total)
