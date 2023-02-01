# 출력초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# nlist = []
# for _ in range(n):
#     nlist.append(int(input()))

# limit = 1
# stack = []
# answer = []
# for nl in nlist:
#     while nl >= limit:
#         stack.append(limit)
#         answer.append('+')
#         limit += 1 
#     try:
#         stack.pop()
#         answer.append('-')
#     except: 
#         answer.append('NO')
#         break

# if answer[-1] == "NO":
#     print("NO")
# else:
#     for a in answer:
#         print(a)

# 성공
import sys
input = sys.stdin.readline
n = int(input())
nlist = []
for _ in range(n):
    nlist.append(int(input()))

limit = 1
stack = []
answer = []
for nl in nlist:
    while nl >= limit:
        stack.append(limit)
        answer.append('+')
        limit += 1
    
    if stack[-1] == nl:
        stack.pop()
        answer.append('-')
    else: 
        print('NO')
        exit(0)

for a in answer:
    print(a)


