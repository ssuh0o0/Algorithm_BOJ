import sys
input = sys.stdin.readline
an,bn,cn = map(int, input().split())
# 시간초과
# divList = []

# for i in range(1,c+1):
#     divList.append((a**i)%c)

# print(divList[b%len(divList)])

# 94퍼 성공
# def div(a,b,c):
#     if b == 1:
#         return a

#     if b % 2 :
#         num = div(a,(b-1)//2,c)
#         return (num * num * a) % c
#     else:
#         num = div(a,b//2,c)
#         return (num * num) % c

# print(div(an, bn, cn))

# 성공 코드
def div(a,b,c):
    if b == 1:
        return a%c

    if b % 2 :
        num = div(a,(b-1)//2,c)
        return (num * num * a) % c
    else:
        num = div(a,b//2,c)
        return (num * num) % c

print(div(an, bn, cn))
    

    


