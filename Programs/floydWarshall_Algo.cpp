#include<bits/stdc++.h>
using namespace std;
#define MAX 20

int dist[MAX][MAX];
int parent[MAX][MAX];

void shortestPath(int i,int j){

	if(i == j){
	
		cout<<char(i+65)<<" ";
		return;
	}
	
	shortestPath(i,parent[i][j]);
	cout<<char(j+65)<<" ";
	
	return ;
}


void floydWarshall(int v,int adj_mat[MAX][MAX]){
	
	for(int i=0;i<v;i++){
	
		for(int j=0;j<v;j++){
			
			if(i == j){
				dist[i][j] = 0;
				parent[i][j] = -1;
			}
			
			else{
				if(adj_mat[i][j] != 0){
					dist[i][j] = adj_mat[i][j];
					parent[i][j] = i;
				}
				
				else{
					dist[i][j] = INT_MAX;
					parent[i][j] = -1;
				}
				
			}
			
		}
		
	}
	
	
	for(int k=0;k<v;k++){
	
		for(int i=0;i<v;i++){
		
			for(int j=0;j<v;j++){
			
				if((dist[i][k] != INT_MAX && dist[k][j] != INT_MAX) && dist[i][k] + dist[k][j] < dist[i][j]){
				
					dist[i][j] = dist[i][k] + dist[k][j]; 
					parent[i][j] = parent[k][j];
				}
				
			}
		}
		
	}
	
	for(int i=0;i<v;i++){
	
		if(dist[i][i] < 0){
		
			cout<<"Negative cycle is present"<<endl;
			return;
		}
	}
	
	
	cout<<"The shortest paths are "<<endl;
	cout<<"-----------------------"<<endl;
	
	for(int i=0;i<v;i++){
		
		for(int j=0;j<v;j++){
			
			cout<<char(i+65)<<" "<<char(j+65)<<"  "<<dist[i][j]<<endl;
			shortestPath(i,j);
			cout<<endl<<endl;
		}
		cout<<"--------------------------"<<endl;
	}
	
	cout<<endl;
	
	
	return ;
	
}


int main(){
	
	system("clear");
	
	freopen("input_floyd.txt","r",stdin);
	
	int v;
	cin>>v;
	
	int adj_mat[MAX][MAX];
	
	for(int i=0;i<v;i++){
	
		for(int j=0;j<v;j++){
		
			cin>>adj_mat[i][j];
		}
	}
	
	cout<<"The Adjacency Matrix is "<<endl;
	
	for(int i=0;i<v;i++){
	
		for(int j=0;j<v;j++){
		
			cout<<adj_mat[i][j]<<" ";
		}
		cout<<endl;
	}
	cout<<endl;
	
	
	
	floydWarshall(v,adj_mat);
	 
	
	return 0;
}
