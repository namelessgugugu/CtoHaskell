// longest increasing subsequence
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    int *s = (int *)malloc(sizeof(int) * n);
    int top = 0;
    for (int i = 0; i < n;++i)
    {
        int a;
        scanf("%d", &a);
        if(top == 0 || a > s[top - 1])
        {
            s[top++] = a;
        }
        else
        {
            for (int j = top - 1; j >= 0;--j)
                if(s[j] < a)
                {
                    s[j + 1] = a;
                    break;
                }
        }
    }
    printf("%d\n", top);
    free(s);
    return 0;
}