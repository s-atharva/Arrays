def find_subsequence_k_after_capping(nums, k):
    flag_array = []
    x = len(nums)

    for x in range(1, x + 1):
        capped = []
        for num in nums:
            if num > x:
                capped.append(x)
            else:
                capped.append(num)
        print(capped)

        flag = False
        for i in range(len(capped)):
            for j in range(i + 1, len(capped)):
                if capped[i] + capped[j] == k:
                    flag = True
                    break
            if flag:
                break
        flag_array.append(flag)
    print(flag_array)


nums = [4, 3, 2, 4]
k = 5
find_subsequence_k_after_capping(nums=nums, k=k)

# nums = [3, 3, 2, 3]
# for i in range(len(nums)):
#     for j in range(1, len(nums)):
#         print(nums[i], nums[j])
