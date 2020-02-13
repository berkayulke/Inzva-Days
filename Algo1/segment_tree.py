tree = int(1e7+8)*[0]

siz = int(input())
ar = [0] + [int(x) for x in input().split()]
que_size = int(input())


def build(ind, lef, rig):
    if lef == rig:
        tree[ind] = ar[lef]
        return
    mi = (lef+rig)//2
    build(ind*2, lef, mi)
    build(ind*2+1, mi+1, rig)
    tree[ind] = tree[ind*2] + tree[ind*2+1]


def que(ind, lef, rig, lef_que, rig_que):
    if lef > rig_que or rig < lef_que:
        return 0
    if lef >= lef_que and rig <= rig_que:
        return tree[ind]
    mi = (lef+rig)//2
    return que(ind*2, lef, mi, lef_que, rig_que) + que(ind*2+1, mi+1, rig, lef_que, rig_que)


# x val yap
def upd(ind, lef, rig, x, val):
    if lef > x or rig < x:
        return
    if lef >= x and rig <= x:
        tree[ind] = val
        return
    mi = (lef+rig)//2
    upd(2*ind, lef, mi, x, val)
    upd(2*ind+1, mi+1, rig, x, val)
    tree[ind] = tree[2*ind] + tree[2*ind+1]

# que(1,1,siz,x,y) -> [x,y] arasi toplam
# upd(1, 1, siz, a, val) -> a. elemani val yap


build(1, 1, siz)

# query al
for _ in range(que_size):
    query = [int(x) for x in input().split()]
    #print(f"query = {query}")
    if query[0] == 1:
        print(que(1, 1, siz, query[1], query[2]))
    else:
        upd(1, 1, siz, query[1], query[2])
