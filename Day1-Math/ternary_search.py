#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-1/challenges/utku-the-lifeguard
from math import sqrt
x1 = x2 = y1 = y1 = v1 = v2 = 0


def f(a):
    global x1, x2, y1, y1, v1, v2
    k = abs(x1-x2) - a
    part1 = sqrt(y1**2 + a**2)/v1
    part2 = sqrt(y2**2 + k**2)/v2
    return part1 + part2

def ter_ser():
    l, r = x1-1e8, x2+1e8
    while (r-l) > 1e-8:
        first = l + (r-l)/3
        second = r - (r-l)/3
        if f(first) < f(second):
            r = second
        else:
            l = first
    return l


t = int(input())
for _ in range(0, t):
    x1, y1, x2, y2, v1, v2 = [int(x) for x in input().split()]
    res = f(ter_ser())
    print(f"{res:.5f}")
