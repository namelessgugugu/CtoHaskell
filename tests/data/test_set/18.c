// Array operations
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int n, q;
    scanf("%d%d", &n, &q);
    int *a = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n;++i)
        scanf("%d", a + i);
    for (int i = 0; i < q;++i)
    {
        int op, l, r;
        scanf("%d%d%d", &op, &l, &r);
        if(op == 1)
        {
            for (int j = l; j < r;++j)
                ++a[j];
        }
        else
        {
            int res = 0;
            for (int j = l; j < r;++j)
                res += a[j];
            printf("%d\n", res);
        }
    }
    free(a);
    return 0;
}