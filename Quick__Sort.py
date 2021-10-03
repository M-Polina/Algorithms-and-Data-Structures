import random


def Sort(nums, l_ind, r_ind):
    pivot_ind = random.randint(l_ind, r_ind)
    pivot = nums[pivot_ind]
    nums[pivot_ind], nums[r_ind] = nums[r_ind], pivot
    last_s_i = l_ind - 1
    for i in range(l_ind, r_ind):
        if (nums[i] <= pivot):
            last_s_i += 1
            nums[last_s_i], nums[i] = nums[i], nums[last_s_i]
    nums[last_s_i + 1], nums[r_ind] = nums[r_ind], nums[last_s_i + 1]
    return (last_s_i + 1)


def Quick_Sort(nums, l_ind, r_ind):
    if (l_ind < r_ind):
        pivot_ind = Sort(nums, l_ind, r_ind)
        Quick_Sort(nums, l_ind, pivot_ind - 1)
        Quick_Sort(nums, pivot_ind, r_ind)


file_in = open("sort.in", "r")
file_out = open("sort.out", "w")
col_nums = int(file_in.readline())
nums = list(map(int, file_in.read().split()))
Quick_Sort(nums, 0, col_nums - 1)
for i in range(col_nums - 2):
    print(nums[i], file=file_out, end=" ")
print(nums[col_nums - 1], file=file_out)
file_out.close()
