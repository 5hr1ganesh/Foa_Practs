# Program to find second largest element in an array using tournament method

import sys

print("Enter size of array")
s = int(input())
i = 0
b = []
print("Enter array of elements")

while i < s:
    b.append(int(input()))
    i = i + 1
    print(b)


def getSecondhighest(b):
    hi = mid = lo = 0
    for i in range(0, len(b)):
        x = b[i]
        if x > hi:
            lo = mid
            mid = hi
            hi = x

        elif hi > x > mid:
            lo = mid

        elif x < lo:
            lo = x

    return mid


print("second highest element in given array=", getSecondhighest(b))
