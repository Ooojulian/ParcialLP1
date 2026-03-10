#include <stdio.h>
#include <time.h>

// algoritmo de euclides recursivo puro 
long long mcd(long long a, long long b) {
    if (b == 0) return a;
    return mcd(b, a % b); // recursividad de cola
}

int main() {
    // medir el tiempo
    clock_t inicio = clock();

    long long resultado = 0;
    
    // toca meterle un ciclo re largo pa poder medir el rendimiento
    // si lo hago una sola vez, c lo hace en 0.00000 segs y no hay analisis
    for(long long i = 1; i <= 50000000; i++) {
        resultado = mcd(12345678, i);
    }

    // paro el reloj
    clock_t fin = clock();
    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("ultimo mcd calculado: %lld\n", resultado);
    printf("tiempo gastado en C: %f segundos\n", tiempo);

    return 0;
}
