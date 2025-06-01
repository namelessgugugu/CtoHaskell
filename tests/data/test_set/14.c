// matrix product
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int **new_matrix(int n, int m)
{
    int **a = (int **)malloc(sizeof(int *) * n);
    for (int i = 0; i < n;++i)
    {
        a[i] = (int *)malloc(sizeof(int) * m);
        memset(a[i], 0, sizeof(int) * m);
    }
    return a;
}
void free_matrix(int **a, int n)
{
    for (int i = 0; i < n;++i)
        free(a[i]);
    free(a);
    return;
}
int main(void)
{
    int n, m, l;
    scanf("%d%d%d", &n, &m, &l);
    int **a = new_matrix(n, m), **b = new_matrix(m, l), **c = new_matrix(n, l);
    for (int i = 0; i < n;++i)
        for (int j = 0; j < m;++j)
            scanf("%d", a[i] + j);
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < l; ++j)
            scanf("%d", b[i] + j);
    for (int i = 0; i < n;++i)
        for (int j = 0; j < m;++j)
            for (int k = 0; k < l;++k)
                c[i][k] += a[i][j] * b[j][k];
    for (int i = 0; i < n;++i)
        for (int j = 0; j < l;++j)
            printf("%d%c", c[i][j], j == l - 1 ? '\n' : ' ');
    free_matrix(a, n);
    free_matrix(b, m);
    free_matrix(c, n);
    return 0;
}