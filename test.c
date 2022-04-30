#include <stdio.h>

void main()
{
    int x;
    printf("Enter a number: ");
    scanf("%d", &x);

    switch (x)
    {
    case 1:
        printf("ONE...");
        break;

    case 2:
        printf("TWO...");
        break;

    case 3:
        printf("THREE...");
        break;

    default:
        printf("Invalid entry...");
    }
}