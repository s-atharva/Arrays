def longest_k_substr(s, k):
    i = 0
    j = 0
    ans = -1
    maps = dict()
    while j < len(s):
        # add char to map
        if s[j] in maps:
            maps[s[j]] += 1
        else:
            maps[s[j]] = 1

        if len(maps) < k:
            j += 1
        elif len(maps) == k:
            if j - i + 1 > ans:
                ans = j - i + 1
            j += 1
        else:  # len(maps) > k
            while len(maps) > k:
                maps[s[i]] -= 1
                if maps[s[i]] == 0:
                    del maps[s[i]]
                i += 1
            j += 1
    return ans


print(longest_k_substr("aabacbebebe", 3))
