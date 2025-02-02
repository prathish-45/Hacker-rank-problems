#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function
    int add, sub;
    if(*a>*b){
     add = *a + *b;
     sub = *a - *b;   
    } else if (*a < *b) {
     add = *a + *b;
     sub = *b - *a;
    }
    *a = add;
    *b = sub;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
