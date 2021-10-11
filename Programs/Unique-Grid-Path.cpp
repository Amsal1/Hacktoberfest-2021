//Unique Grid Path
#include <bits/stdc++.h>
using namespace std;

//Method: Using Dynamic Programming
//T.C->O(N*M) & S.C->O(N*M)
int dp[101][101];
int countPaths(int i, int j, int n, int m)
{
    if (i == n - 1 && j == m - 1)
    {
        return 1;
    }
    if (i >= n || j >= m)
    {
        return 0;
    }
    if (dp[i][j] != -1)
    {
        return dp[i][j];
    }
    return dp[i][j] = countPaths(i, j + 1, n, m) + countPaths(i + 1, j, n, m);
}

int uniquePaths(int m, int n)
{
    for (int i = 0; i < 101; i++)
    {
        for (int j = 0; j < 101; j++)
        {
            dp[i][j] = -1;
        }
    }
    return countPaths(0, 0, m, n);
} 

int main()
{
    int n, m;
    cin >> m >> n;
    //m: rows
    //n:columns
    int uniquepaths = uniquePaths(m, n);
    cout << "Total Unique Paths are: " << uniquepaths << endl;
    return 0;
}