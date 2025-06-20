// prefix sum
#include <stdio.h>
#include <stdlib.h>
int n;
int main(void)
{
    scanf("%d", &n);
    int *a = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n;++i)
        scanf("%d", a + i);
    for (int i = 1; i < n;++i)
        a[i] += a[i - 1];
    for (int i = 0; i < n;++i)
        printf("%d\n", a[i]);
    free(a);
    return 0;
}