import sys
s = sys.stdin.readline()
q = int(sys.stdin.readline())

alphaArr = [[0] * 26 for _ in range(len(s)+1)]

for idx, char in enumerate(s):
    c = ord(char) - ord("a")
    for j in range(26):
        if c == j:
            alphaArr[idx+1][j] = alphaArr[idx][j] + 1
            continue
        alphaArr[idx+1][j] = alphaArr[idx][j]

for _ in range(q):
    a,l,r = sys.stdin.readline().split()
    a = ord(a) - ord("a")
    print(alphaArr[(int)(r)+1][a] - alphaArr[(int)(l)][a] )