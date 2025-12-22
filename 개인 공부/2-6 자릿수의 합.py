n = int(input())
numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    numbers[i] = str(numbers[i])

split_num = []
for i in numbers:
    split_num.append(list(i))

for i in range(len(split_num)):
    for j in range(len(split_num[i])):
        split_num[i][j] = int(split_num[i][j])

sum_num = []
for i in split_num:
    sum_num.append(sum(i))

max_sum = max(sum_num)
for i in range(len(sum_num)):
    if sum_num[i] == max_sum:
        print(numbers[i])