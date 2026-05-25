#include <stdio.h>
int main(){
    int y1,y2,m2,m1,d1,d2;
    scanf("%d%d%d%d%d%d",&y1,&y2,&m1,&m2,&d2,&d1);
    d1 += 372*y1+31*m1-31 , d2 += 372*y2+31*m2-31;
    if(d1>d2) printf("2");
    else if(d1<d2) printf("1");
    else printf("0");
}
