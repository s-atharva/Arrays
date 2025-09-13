def count_occurrences_anagrams(text, pattern):
    i = 0
    j = 0
    k = len(pattern)
    char_count = {}
    n = len(text)

    result = 0
    # 1. count of each alphabet
    for char in pattern:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    count = len(char_count)

    while j < n:
        if text[j] in char_count:
            char_count[text[j]] -= 1
            if char_count[text[j]] == 0:
                count -= 1
        # if size is not yet reached
        if j - i + 1 < k:
            j += 1
        # if window size reach
        elif j - i + 1 == k:
            if count == 0:
                result += 1
            if text[i] in char_count:
                if char_count[text[i]] == 0:
                    count += 1
                char_count[text[i]] += 1

            i += 1
            j += 1
    return result


text = "aabaabaa"
pattern = "aaba"

print(count_occurrences_anagrams(text=text, pattern=pattern))
