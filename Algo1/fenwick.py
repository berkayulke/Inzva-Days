tree = int(1e6+1)*[0]

siz = int(input())
ar = [0] + [int(x) for x in input().split()]
que_size = int(input())


def build():
    for i in range(1, siz+1):
        add(i, ar[i])


def add(ind, val):
    while ind <= siz:
        tree[ind] += val
        ind += ind & (-ind)


# 1'den indekse olanlari verir
def one_to(x):
    res = 0
    while x >= 1:
        res += tree[x]
        x -= x & (-x)
    return res


def update(ind, val):
    add(ind, val-ar[ind])
    ar[ind] = val


def que(lef, rig):
    return one_to(rig) - one_to(lef-1)


build()
for _ in range(que_size):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        print(que(query[1], query[2]))
    else:
        update(query[1],query[2])