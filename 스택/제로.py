import sys
n = int(sys.stdin.readline())
nlist = []
for _ in range(n):
    num = int(sys.stdin.readline())
    nlist.append(num) if num != 0 else nlist.pop()

print(sum(nlist))