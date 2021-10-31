#include<stdio.h>
void main()
{
int s[9],j,i,c,n;
printf("enter limit of array");
scanf("%d",&n);
printf("enter array");
for(i=0;i<n;i++)
{
scanf("%d",&s[i]);}
for(i=0;i<n-1;i++)
{
for(j=0;j<(n-i-1);j++)
{
if(s[j]>s[j+1])
{
c=s[j];
s[j]=s[j+1];
s[j+1]=c;
}}
}
for(i=0;i<n;i++)
{
printf("%d\t",s[i]);}
}