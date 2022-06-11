N = int(input())

countIn = 0
countOut = 0

for i in range(N):
    if (10 <= int(input()) <= 20):
        countIn += 1
    else:
        countOut += 1

print('%i in' %countIn)
print('%i out' %countOut)