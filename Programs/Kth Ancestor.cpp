#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int vec[100000],pnt[200000][19],i,root,fg,tst,num,que,p,q;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int opt,anc,cnt;
    scanf("%d",&tst);
    while(tst--){
        scanf("%d",&num);
        memset(pnt,0,sizeof(pnt));
        for(i=0;i<num;i++){
            scanf("%d%d",&p,&q);
            vec[i]=p;
            if(q!=0)
                pnt[p][0]=q;
        }
        
        for(root=0;root<18;root++)
            for(i=0;i<num;i++){
                fg=vec[i];
                pnt[fg][root+1]=pnt[pnt[fg][root]][root];
            }
        scanf("%d",&que);
        for(i=0;i<que;i++){
            scanf("%d",&opt);
            if(opt==0) {
                scanf("%d%d",&p,&q);
                pnt[q][0]=p;
                for(root=0;root<18;root++)
                    pnt[q][root+1]=pnt[pnt[q][root]][root];}
            else if(opt==1){
                scanf("%d",&p);
                pnt[p][0]=0;}
            else {
                scanf("%d%d",&p,&anc);
                if(pnt[p][0] == 0){
                    printf("0\n");
                    continue;}
                cnt=0;
                while(anc){
                    if(anc%2==1)
                        p=pnt[p][cnt];
                    if(p==0)
                        break;
                    anc=anc/2;
                    cnt++;}
                printf("%d\n",p);}}
    }
    return 0;

}
