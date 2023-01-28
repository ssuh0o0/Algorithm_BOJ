import sys
n = int(sys.stdin.readline())

def isCorrectBracket(bra):
    check = []
    for b in bra:
        if b == "(":
            check.append(b)
        else:
            if len(check) > 0:
                check.pop()
            else:
                return "NO"
    return "YES" if len(check) == 0 else "NO"

for _ in range(n):
    print(isCorrectBracket(sys.stdin.readline().strip()))