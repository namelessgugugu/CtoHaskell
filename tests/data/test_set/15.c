// faster max segment sum
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    int *a = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i)
        scanf("%d", a + i);
    int ans = INT_MIN, now = 0;
    for (int i = 0; i < n; ++i)
    {
        now += a[i];
        if(now > ans)
            ans = now;
        if(now < 0)
            now = 0;
    }
    printf("%d\n", ans);
    free(a);
    return 0;
}
