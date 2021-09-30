import random

def Merge(A, p, q,  r):

    n1 = q - p + 1
    n2 = r - q
    L = [0]
    R = [0]
    for i in range(1,n1+1):
        L.append(A[p+i-1])
    for j in range(1,n2+1):
        R.append(A[q+j])
    L.append(1000000000000000000000000000000000000000000000000000000000000)
    R.append(1000000000000000000000000000000000000000000000000000000000000)
    i = 1
    j = 1
    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1

def Merge_Sort(A, p, r):
    if p>=r:
        return
    q=(p+r)//2
    Merge_Sort(A, p, q)
    Merge_Sort(A, q+1, r)
    Merge(A,p,q,r)



f = open("sort.in")
fout = open("sort.out", "w")
n = int(f.readline())
numbers = list(map(int, f.readline().split()))
Merge_Sort(numbers, 0, n-1)
for i in range(0, n-1):
    print(numbers[i], file = fout, end = " ")
print(numbers[n-1], file = fout, end = "")
fout.close()