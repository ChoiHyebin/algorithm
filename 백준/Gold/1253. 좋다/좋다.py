n = int(input())
num = sorted(list(map(int, input().split())))

cnt = 0

for i in range(n):
    good = num[i]
    start = 0
    end = len(num) - 1

    while start < end:
        if num[start] + num[end] == good:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                cnt += 1
                break
        elif num[start] + num[end] > good:
            end -= 1
        elif num[start] + num[end] < good:
            start += 1

print(cnt)