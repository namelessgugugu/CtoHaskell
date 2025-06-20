// floyd
#include <stdio.h>
#include <stdlib.h>
int n;
int main(void)
{
    scanf("%d", &n);
    int **a = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n;++i)
    {
        a[i] = (int *)malloc(n * sizeof(int));
        for (int j = 0; j < n;++j)
            scanf("%d", a[i] + j);
    }
    for (int k = 0; k < n;++k)
        for (int i = 0; i < n;++i)
            for (int j = 0; j < n;++j)
                if(a[i][j] <= a[i][k] + a[k][j])
                    a[i][j] = a[i][k] + a[k][j];
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
            printf("%d%c", a[i][j], j == n - 1 ? '\n' : ' ');
    }
    for (int i = 0; i < n; ++i)
        free(a[i]);
    free(a);
    return 0;
}