import sys
input = sys.stdin.readline

a,b,c = list(map(int, input().split()))

dict = {}
def w(a,b,c):
    if (a,b,c) in dict:
        return dict[a,b,c]

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    elif a < b and b < c:
        dict[a,b,c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dict[a,b,c]
    else:
        dict[a,b,c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dict[a,b,c]

while a != -1 or b != -1 or c != -1:
    print(f'w({a}, {b}, {c}) =',w(a,b,c))
    a,b,c = list(map(int, input().split()))