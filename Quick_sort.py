import random

def QuickSort(nums):
   if len(nums) <= 1:
       return nums
   else:
       random_pivot_element = random.choice(nums)
       smaller_nums = []
       same_nums = []
       bigger_nums = []
       for n in nums:
           if n < random_pivot_element:
               smaller_nums.append(n)
           elif n > random_pivot_element:
               bigger_nums.append(n)
           else:
               same_nums.append(n)
       return QuickSort(smaller_nums) + same_nums + QuickSort(bigger_nums)

f = open("sort.in")
fout = open("sort.out", "w")
n = int(f.readline())
numbers = list(map(int, f.readline().split()))
numbers = QuickSort(numbers)
for i in range(0, n-1):
    print(numbers[i], file = fout, end = " ")
print(numbers[n-1], file = fout, end = "")
fout.close()