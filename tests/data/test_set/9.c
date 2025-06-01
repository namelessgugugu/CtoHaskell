// merge sort
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void merge_sort(int n, int *a, int *buf)
{
    if(n == 1)
    {
        return;
    }
    int m = n / 2;
    merge_sort(m, a, buf);
    merge_sort(n - m, a + m, buf);
    int p = 0, q = m;
    for (int i = 0; i < n;++i)
    {
        if(p == m)
            buf[i] = a[q++];
        else if(q == n)
            buf[i] = a[p++];
        else if(a[p] <= a[q])
            buf[i] = a[p++];
        else
            buf[i] = a[q++];
    }
    memcpy(a, buf, sizeof(int) * n);
    return;
}
int main(void)
{
    int n;
    scanf("%d", &n);
    int *a = (int *)malloc(sizeof(int) * n);
    int *b = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n;++i)
        scanf("%d", a + i);
    merge_sort(n, a, b);
    for (int i = 0; i < n;++i)
        printf("%d\n", a[i]);
    free(a);
    free(b);
    return 0;
}