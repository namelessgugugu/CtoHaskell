// is prime
#include <stdio.h>
int n;
int main(void)
{
    scanf("%d", &n);
    for (int i = 2; (long long)i * i <= n;++i)
        if(n % i == 0)
        {
            puts("Not Prime!");
            return 0;
        }
    puts("Is Prime!");
    return 0;
}