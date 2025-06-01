// gcd
#include <stdio.h>
int gcd(int x, int y)
{
    return y == 0 ? x : gcd(y, x % y);
}
int main(void)
{
    int n, m;
    scanf("%d%d", &n, &m);
    printf("%d %lld\n", gcd(n, m), (long long)n * m / gcd(n, m));
    return 0;
}