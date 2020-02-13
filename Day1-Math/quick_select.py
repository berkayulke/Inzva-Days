#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-1/challenges/trees-5
import random
from math import inf


def partition(arr, l, r):
    piv = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] >= piv:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def q_sel(arr, l, r, k):
    ind = partition(arr, l, r)
    if ind - l == k-1:
        return arr[ind]
    elif ind-l > k-1:
        return q_sel(arr, l, ind-1, k)
    else:
        return q_sel(arr, ind+1, r, k-ind+l-1)

k = int(input())
n = int(input())
a = [int(x) for x in input().split()]
print(q_sel(a,0,len(a)-1,k))
