import sys
input = sys.stdin.readline

def isCorrectBracket2(sline):
    bracket = []

    for s in sline:
        if s == "(" or s == "[":
            bracket.append(s)
        elif s == ")" or s == "]":
            if len(bracket) != 0:
                b = bracket.pop()
                if not ((b == "(" and s == ")") or  (b == "[" and s == "]")):
                    return "no"
            else:
                return "no"
    return "yes" if len(bracket) == 0 else "no"

sline=""
while True:
    sline = input().rstrip()
    if sline == ".":
        break
    print(isCorrectBracket2(sline))       
