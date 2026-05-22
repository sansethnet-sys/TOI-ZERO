#include <iostream>
#include <string>
using namespace std;
int main(){
    cin.tie(0)->sync_with_stdio(0);
    string Hs = "",tf = "XP";
    int A,B,C;
    for(cin>>A>>A ; A ; A = C){
        cin >> B >> C;
        Hs.push_back(tf[A == B]);
    }
    int N = Hs.length();
    while(N) cout<< N-- << Hs[N] <<'\n';
}
