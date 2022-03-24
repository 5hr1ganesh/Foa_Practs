# find smallest and largest elements in an array A using selection algorithm.
import sys
print("Enter size of array")
s = int(input())
i = 0
b = []
print("Enter array")
while i < s:
    b.append(int(input()))
    i = i + 1

print("Array u entered is: \n", b)

for i in range(len(b)):
    minx = i
    for j in range(i+1, len(b)):
        if b[minx]>b[j]:
            minx = j
            b[i], b[minx] = b[minx], b[i]

print("Sorted Array")
for i in range(len(b)):
    print("%d"%b[i]),

print("Smallest Element:%d"%b[0])
print("Largest Element:%d"%b[s-1])

