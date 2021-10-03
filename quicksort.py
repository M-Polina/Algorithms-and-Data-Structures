import random


def QuickSort(nums, left_index, right_index):
    if left_index >= right_index:
        return 0
    pivot_element_index = random.randint(left_index, right_index)
    pivot_element = nums[pivot_element_index]
    nums[pivot_element_index], nums[right_index] = nums[right_index], nums[pivot_element_index]
    last_smaller_element_index = left_index - 1
    for compared_element_index in range(left_index, right_index):
        if nums[compared_element_index] <= pivot_element:
            last_smaller_element_index += 1
            nums[compared_element_index], nums[last_smaller_element_index] = nums[last_smaller_element_index], \
                                                                             nums[compared_element_index]
    nums[last_smaller_element_index + 1], nums[right_index] = nums[right_index], nums[1 + last_smaller_element_index]
    QuickSort(nums, left_index, last_smaller_element_index)
    QuickSort(nums, last_smaller_element_index + 2, right_index)


f = open("sort.in")
fout = open("sort.out", "w")
n = int(f.readline())
numbers = list(map(int, f.readline().split()))
QuickSort(numbers, 0, n - 1)
for i in range(0, n - 1):
    print(numbers[i], file=fout, end=" ")
print(numbers[n - 1], file=fout, end="")
fout.close()
