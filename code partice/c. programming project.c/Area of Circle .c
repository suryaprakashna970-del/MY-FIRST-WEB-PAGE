#include <stdio.h>
#include <math.h>
int main() {
   const float PI = 3.14159265358979323846;
    float radius;
    printf("Enter the radius of the circle: ");
    scanf("%f", &radius);
          float area = PI * radius * radius;
        printf("The area of the circle with radius %.2f is %.2f\n", radius, area);
    

    return 0;
}


