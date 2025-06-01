// change radix to 2
#include <stdio.h>
int n;
int main(void)
{
    scanf("%d", &n);
    if(n == 0)
    {
        puts("0");
        return 0;
    }
    if(n < 0)
    {
        putchar('-');
        n = -n;
    }
    int s[50] = {}, top = 0;
    while(n > 0)
    {
        s[top++] = n % 2;
        n /= 2;
    }
    while(top > 0)
        putchar('0' + s[--top]);
    putchar('\n');
    return 0;
}