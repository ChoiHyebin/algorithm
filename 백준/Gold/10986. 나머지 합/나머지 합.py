n, m = map(int, input().split())
num = list(map(int, input().split()))
sum = 0
r = [0] * m

for i in range(n):
    sum += num[i]
    r[sum%m] += 1

res = r[0]
for i in r:
    res += i*(i-1)//2

print(res)