import math


def Merge(nums, l_ind, r_ind, m):
    l_arr = []
    r_arr = []
    for i in range(l_ind, m + 1):
        l_arr.append(nums[i])
    for i in range(m + 1, r_ind + 1):
        r_arr.append(nums[i])
    l_arr.append(10000000000000)
    r_arr.append(10000000000000)
    l = 0
    r = 0
    for i in range(l_ind, r_ind + 1):
        if (l_arr[l] <= r_arr[r]):
            nums[i] = l_arr[l]
            l += 1
        else:
            nums[i] = r_arr[r]
            r += 1


def Merge_Sort(nums, l_ind, r_ind):
    if (l_ind < r_ind):
        m = (l_ind + r_ind) // 2
        Merge_Sort(nums, l_ind, m)
        Merge_Sort(nums, m + 1, r_ind)
        Merge(nums, l_ind, r_ind, m)


file_in = open("sort.in", "r")
file_out = open("sort.out", "w")
col_nums = int(file_in.readline())
nums = list(map(int, file_in.read().split()))
Merge_Sort(nums, 0, col_nums - 1)
for i in range(col_nums - 2):
    print(nums[i], file=file_out, end=" ")
print(nums[col_nums - 1], file=file_out)
file_out.close()
