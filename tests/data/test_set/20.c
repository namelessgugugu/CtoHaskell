// Kmp
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(void)
{
    int n, m;
    scanf("%d%d", &n, &m);
    char *s = (char *)malloc(sizeof(char) * (n + 1));
    char *t = (char *)malloc(sizeof(char) * (m + 1));
    scanf("%s", s);
    scanf("%s", t);
    int *next = (int *)malloc(sizeof(int) * n);
    next[0] = -1;
    for (int i = 1; i < n;++i)
    {
        int j = next[i - 1];
        while(j != -1 && s[j + 1] != s[i])
            j = next[j];
        next[i] = j + (s[j + 1] == s[i] ? 1 : 0);
    }
    for (int i = 0, pt = -1; i < m;++i)
    {
        while(pt != -1 && t[i] != s[pt + 1])
            pt = next[pt];
        pt += t[i] == s[pt + 1] ? 1 : 0;
        if(pt == n - 1)
        {
            printf("Found at index %d.", i - n + 1);
            free(next);
            free(s);
            free(t);
            return 0;
        }
    }
    puts("Not Found.");
    free(next);
    free(s);
    free(t);
    return 0;
}