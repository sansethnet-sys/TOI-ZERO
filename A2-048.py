N , St = int(input()) , list(map(int,input().split()))
print("Student:"+''.join([" Student"+str(i+1) for i in range(N)]))
if N : 
    mx , mn , av = max(St) , min(St) , sum(St)/N
    print("Highest score:",mx)
    print("Lowest score:",mn)
    print(f"Average score: {av:.1f}")
    print("Students who scored above average:")
    for i , sc in enumerate(St):
        if sc>av : print("Student",1+i)