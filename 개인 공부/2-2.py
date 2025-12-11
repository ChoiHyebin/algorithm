T = int(input()) # test case 수

for t in range(T): #test case 수만큼
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a[s-1:e])
    print("#%d %d" %(t+1, a[k-1]))