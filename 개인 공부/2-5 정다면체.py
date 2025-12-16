N, M = map(int, input().split())

hap = []
for i in range(1, N+1):
    for j in range(1, M+1):
        hap.append(i+j)

#print("hap", hap)
set_hap = list(set(hap))
#print("set_hap", set_hap)

hap_cnt = []
for i in set_hap:
    hap_cnt.append(hap.count(i))

#print("hap_cnt", hap_cnt)

max_cnt = max(hap_cnt) #가장 높은 빈도수
max_num = [] #빈도수가 가장 높은 수를 담기 위한 것
max_num_idx = []

for i in range(len(hap_cnt)):
    if hap_cnt[i] == max_cnt:
        max_num_idx.append(i)

for i in max_num_idx:
    max_num.append(set_hap[i])


for i in max_num:
    print(i, end = ' ')