// Knapsack problem
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void)
{
    int n, v;
    scanf("%d%d", &n, &v);
    int *f = (int *)malloc(sizeof(int) * (v + 1));
    memset(f, 0, sizeof(int) * (v + 1));
    for (int i = 0; i < n;++i)
    {
        int c, w;
        scanf("%d%d", &c, &w);
        for (int j = v; j >= c;--j)
            if(f[j - c] + w > f[j])
                f[j] = f[j - c] + w;
    }
    printf("%d\n", f[v]);
    free(f);
    return 0;
}