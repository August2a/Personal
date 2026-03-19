#include <stdio.h>

int soma(int a, int b) {
    return a + b;
}

int main() {
    int x = 10;
    int y = 20;
    int resultado = soma(x, y);
    printf("Resultado: %d\n", resultado);
    return 0;
}
