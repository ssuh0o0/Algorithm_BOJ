import sys
n = int(sys.stdin.readline())
nlist = []
for _ in range(n):
    order = list(sys.stdin.readline().split())
    if order[0] == "push":
        nlist.append(int(order[1]))
    elif order[0] == "pop":
        print(nlist.pop()) if len(nlist) > 0 else print(-1)
    elif order[0] == "top":
        print(-1) if len(nlist) == 0 else print(nlist[-1])
    elif order[0] == "size":
        print(len(nlist))
    elif order[0] == "empty":
        print(1) if len(nlist) == 0 else print(0)

