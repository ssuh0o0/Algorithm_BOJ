#15651
# import sys
# input = sys.stdin.readline
# n, m = list(map(int, input().split()))
# nlist = []

# def dfs():
#     if len(nlist) == m:
#         print(' '.join(map(str, nlist)))
#         return

#     for i in range(1, n+1):
#         nlist.append(i)
#         dfs()
#         nlist.pop()

# dfs()

import sys
input = sys.stdin.readline
import itertools

N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]
    
for num in itertools.product(num_list, repeat = M):
    for i in num:
        print(i, end = ' ')
    print(end = '\n')