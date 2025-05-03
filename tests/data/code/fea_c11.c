#include <stdio.h>

int main()
{
    struct
    {
        int x;
        int y;
    } point = {.x = 5, .y = 10}; // 匿名结构体

    _Generic(point, struct { int x; int y; }: printf("Point: (%d, %d)\n", point.x, point.y),
        default: printf("Invalid data type!\n")); // 泛型选择表达式

    return 0;
}