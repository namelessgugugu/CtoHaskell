// Dijkstra
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void)
{
    int n;
    scanf("%d", &n);
    int *distance = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n;++i)
        distance[i] = INT_MAX;
    int **w = (int **)malloc(sizeof(int *) * n);
    for (int i = 0; i < n;++i)
    {
        w[i] = (int *)malloc(sizeof(int) * n);
        for (int j = 0; j < n;++j)
            scanf("%d", w[i] + j);
    }
    int *visited = (int *)malloc(sizeof(int) * n);
    memset(visited, 0, sizeof(int) * n);
    distance[0] = 0;
    for (int i = 0; i < n;++i)
    {
        int x = -1;
        for (int j = 0; j < n;++j)
            if(!visited[j] && (x == -1 || distance[j] < distance[x]))
                x = j;
        visited[x] = 1;
        if(distance[x] == INT_MAX)
            continue;
        for (int y = 0; y < n;++y)
            if(distance[y] > distance[x] + w[x][y])
                distance[y] = distance[x] + w[x][y];
    }
    printf("%d\n", distance[n - 1]);
    free(visited);
    free(distance);
    for (int i = 0; i < n;++i)
        free(w[i]);
    free(w);
    return 0;
}