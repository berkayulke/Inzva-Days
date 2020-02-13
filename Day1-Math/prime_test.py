#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-1/challenges/prime-or-not-8-1/submissions
n = int(input())
i = 2
while i*i <= n:
    if n % i == 0:
        print("NO")
        exit()
        quit()
    i+=1
print("YES")
