sm , nm , N = 0 , 0 , int(input())
for i in list(map(int,input().split())):
    nm , sm = nm+i%2 , sm+i
print("SUM",sm,"\nEVEN",N-nm,"\nODD",nm)