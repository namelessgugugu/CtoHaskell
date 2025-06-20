// max segment sum
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    int *a = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i)
        scanf("%d", a + i);
    int ans = INT_MIN;
    for (int i = 0; i < n; ++i)
    {
        int sum = 0;
        for (int j = i; j < n; ++j)
        {
            sum += a[j];
            if (sum > ans)
                ans = sum;
        }
    }
    printf("%d\n", ans);
    free(a);
    return 0;
}
