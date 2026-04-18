N , M = map(int,input().split())
if N-1 in range(10) and M in range(1,21):
    sm , mx = [0]*N , [0]*N
    for k in range(N):
        tmp = list(map(int,input().split()))
        sm[k] , mx[k] = sum(it for it in tmp) , max(tmp)
    for k in range(N):
        print(f"Team {1+k}: Average = {sm[k]/M:.2f}, Max =",mx[k])
    print("Total Score of All Teams =",sum(sm))
else: print("Data Incorrect")