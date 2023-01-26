import sys

formula = list(sys.stdin.readline().split('-'))

digits = []

for f in formula:
    digits.append(sum(map(int,f.split('+'))))

print(2*digits[0] - sum(digits))