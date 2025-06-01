// fib
#include <stdio.h>
int main(void)
{
    int n;
    scanf("%d", &n);
    int a = 0, b = 1;
    for (int i = 1; i < n;++i)
    {
        int c = a + b;
        a = b;
        b = c;
    }
    printf("%d\n", b);
    return 0;
}