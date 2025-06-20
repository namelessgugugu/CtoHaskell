// quick sort
#include <stdio.h>
#include <stdlib.h>
void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
    return;
}
void quick_sort(int n, int *a)
{
    if(n <= 1)
        return;
    int k = a[0];
    int p = 0, q = n - 1;
    while(p < q)
    {
        while(q > p && a[q] >= k)
            --q;
        if(p == q)
            break;
        swap(a + p, a + q);
        while(p < q && a[p] <= k)
            ++p;
        if(p == q)
            break;
        swap(a + p, a + q);
    }
    quick_sort(p, a);
    quick_sort(n - p - 1, a + p + 1);
    return;
}

int main(void)
{
    int n;
    scanf("%d", &n);
    int *a = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i)
        scanf("%d", a + i);
    quick_sort(n, a);
    for (int i = 0; i < n; ++i)
        printf("%d\n", a[i]);
    free(a);
    return 0;
}