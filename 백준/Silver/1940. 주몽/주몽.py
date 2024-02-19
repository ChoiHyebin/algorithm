n = int(input())
m = int(input())
num = list(map(int, input().split()))

num.sort()
left = 0
right = len(num) - 1
cnt = 0

while left < right:
    sum = num[left] + num[right]
    if sum < m:
        left += 1
    elif sum > m:
        right -= 1
    else:
        cnt += 1
        left += 1
        right -= 1

print(cnt)