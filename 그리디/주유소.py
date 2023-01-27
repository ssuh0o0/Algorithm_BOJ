# 17점
import sys
n = map(int,sys.stdin.readline())
lens = list(map(int,sys.stdin.readline().split()))
liters = list(map(int,sys.stdin.readline().split()))

minLidx = 0
minLiter = 10000
for i in range(len(liters)-1):
    if minLiter > liters[i]:
        minLidx = i
        minLiter = liters[i]

answer = 0
totalLength = sum(lens)
for j in range(minLidx):
    answer += lens[j] * liters[j]
    totalLength -= lens[j]

print(answer+totalLength*minLiter)

# 100점  
import sys
n = map(int,sys.stdin.readline())
lens = list(map(int,sys.stdin.readline().split()))
liters = list(map(int,sys.stdin.readline().split()))

answer = 0
minLiter = 1000000000  # minLiter = 10000 #58점
for i in range(len(liters)-1):
    if minLiter > liters[i]:
        minLiter = liters[i]
    answer += minLiter * lens[i]

print(answer)
