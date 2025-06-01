// custom structure
#include <stdio.h>
#include <string.h>
struct Node
{
    int x, y;
};
int main(void)
{
    struct Node p, q;
    scanf("%d%d", &p.x, &p.y);
    scanf("%d%d", &q.x, &q.y);
    long long distance = (long long)(p.x - q.x) * (p.x - q.x) + (long long)(p.y - q.y) * (p.y - q.y);
    printf("%lld\n", distance);
    return 0;
}