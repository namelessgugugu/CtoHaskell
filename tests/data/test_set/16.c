// Luogu P1030 (URL: https://www.luogu.com.cn/problem/P1030)

#include <stdio.h>
#include <stdlib.h>
int *m, *h, *result, cnt;
void dfs(int ms, int me, int hs, int he)
{
    if (hs > he || ms > me)
        return;
    result[cnt++] = h[he];
    if (hs == he)
        return;
    int i;
    for (i = ms; i <= me; i++)
    {
        if (m[i] == h[he])
        {
            dfs(ms, i - 1, hs, hs + i - 1 - ms);
            dfs(i + 1, me, he - me + i, he - 1);
            return;
        }
    }
    return;
}
int main()
{
    int n;
    scanf("%d", &n);
    m = (int *)malloc(sizeof(int) * n);
    h = (int *)malloc(sizeof(int) * n);
    result = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n;++i)
        scanf("%d", m + i);
    for (int i = 0; i < n; ++i)
        scanf("%d", h + i);
    dfs(0, n - 1, 0, n - 1);
    for (int i = 0; i < n;++i)
        printf("%d%c", result[i], i == n - 1 ? '\n' : ' ');
    free(m);
    free(h);
    free(result);
    return 0;
}
