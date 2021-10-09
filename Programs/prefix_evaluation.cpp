#include <iostream>
using namespace std;
#include<bits/stdc++.h>

int operate(int a,int b,char c){
    if(c=='+'){
        return a+b;
    }
    else if(c=='-'){
        return a-b;
    }
    else if(c=='*'){
        return a*b;
    }
    else if(c=='/'){
        return a/b;
    }
    else if(c=='^'){
        return a^b;
    }
}
int main() {
    int op1,op2,top=-1,value=0;
    vector<int> v;
    string post;
    cin>>post;
    // cout<<post<<endl;
    int i=post.size()-1;
    char tmp;
    while(post[i]){
        tmp=post[i];
        if(post[i]=='+' || post[i]=='-' || post[i]=='*' || post[i]=='/' || post[i]=='^'){
            value=operate(v[top],v[top-1],tmp);
            v.pop_back();
            v.pop_back();
            top-=2;
            v.push_back(value);
            top++;
        }
        else{
            int n=(int)tmp-'0';
            v.push_back(n);
            top++;
        }
        i--;
    }
    cout<<v[top]<<endl;
	return 0;
}
