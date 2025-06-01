// sieve
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void)
{
    int n;
    scanf("%d", &n);
    int *a = (int *)malloc(sizeof(int) * (n + 1));
    memset(a, 0, sizeof(int) * (n + 1));
    for (int i = 2; i <= n; ++i)
    {
        if(!a[i])
        {
            printf("%d\n", i);
            for (int j = i + i; j <= n; j += i)
                a[j] = 1;
        }
    }
    free(a);
    return 0;
}