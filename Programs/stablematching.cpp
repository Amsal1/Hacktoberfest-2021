#include <stdio.h>
#include <stdlib.h>
#define N 1000

int wPrefersM1OverM(int prefer[2 *N][N], int w, int m, int m1, int a)
{
	for (int i = 0; i < a; i++)
	{ 
		if (prefer[w][i] == m1)
			return 1;

		if (prefer[w][i] == m)
			return 0;
	}
}

void stableMarriage(int prefer[2 *N][N], int a)
{
	int size = a;
	int wPartner[N];
	for (int i = 0; i < N; i++)
		wPartner[i] = -1;

	int mFree[N] = { 0 };
	int freeCount = a;

	while (freeCount > 0)
	{
		int m;
		for (m = 0; m < a; m++)
			if (mFree[m] == 0)
				break;
		for (int i = 0; i < a && mFree[m] == 0; i++)
		{
			int w = prefer[m][i];

			if (wPartner[w - a] == -1)
			{
				wPartner[w - a] = m;
				mFree[m] = 1;
				freeCount--;
			}
			else	 
			{
				int m1 = wPartner[w - a];

				if (wPrefersM1OverM(prefer, w, m, m1, a) == 0)
				{
					wPartner[w - a] = m;
					mFree[m] = 1;
					mFree[m1] = 0;
				}
			}
		}
	}

	printf("W   M\n");
	for (int i = 0; i < a; i++)
		printf(" %d    %d\n", i + a, wPartner[i]);

}

int main()
{
	int testcases;
	scanf("%d", &testcases);

	while (testcases-- > 0)
	{
		int a;
		scanf("%d", &a);
		int prefer[2 *N][N];
		for (int i = 0; i < 2 * a; i++)
		{
			for (int j = 0; j < a; j++)
			{
				int jj;
				scanf("%d", &jj);
				prefer[i][j] = jj;
			}
		}

		stableMarriage(prefer, a);
	}

	return 0;
}
/
