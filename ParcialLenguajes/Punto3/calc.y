%{

#include <stdio.h>
#include <stdlib.h>

// variables externas de flex
extern FILE *yyin;
int yylex(void);
void yyerror(char *s);

// declaro mi funcion de la raiz
double hacer_newton(double numero);
%}

%union {
    double val;
}

%token <val> NUM
%token RAIZ FIN
%type <val> operacion

// precedencia pa que no multiplique antes de sumar y se tire todo
%left '+' '-'
%left '*' '/'

%%

todo:
    | todo linea
    ;

linea:
    operacion FIN { printf("=> el resultado es: %f\n", $1); }
    | FIN         { /* enter vacio */ }
    ;

operacion:
    NUM { $$ = $1; }
    | RAIZ '(' operacion ')' { $$ = hacer_newton($3); }
    | operacion '+' operacion { $$ = $1 + $3; }
    | operacion '-' operacion { $$ = $1 - $3; }
    | operacion '*' operacion { $$ = $1 * $3; }
    | operacion '/' operacion {
        if($3 == 0) {
            printf("bro, no dividas por cero\n");
            $$ = 0;
        } else {
            $$ = $1 / $3;
        }
    }
    | '(' operacion ')' { $$ = $2; }
    ;

%%

// calculo de la raiz por newton raphson a la fuerza bruta
double hacer_newton(double n) {
    if(n < 0) {
        printf("error: raiz de numero negativo no existe en los reales\n");
        return 0;
    }
    if(n == 0) return 0;
    
    double x_actual = n;
    double x_nuevo = 0;
    
    // printf("debug: calculando raiz de %f\n", n); // lo dejo comentado pa que vea que probe
    
    // le meto 1000 iteraciones por si acaso, igual converge rapido
    for(int i = 0; i < 1000; i++) {
        x_nuevo = 0.5 * (x_actual + (n / x_actual));
        
        // saco valor absoluto manual sin usar librerias
        double resta = x_actual - x_nuevo;
        if(resta < 0) resta = resta * -1;
        
        // tolerancia pa que pare si ya es casi igual
        if(resta < 0.000001) {
            break;
        }
        x_actual = x_nuevo;
    }
    
    return x_nuevo;
}

void yyerror(char *s) {
    printf("error de sintaxis: %s\n", s);
}

int main(int argc, char **argv) {
    // aca controlo que entre un archivo .txt si o si
    if(argc > 1) {
        FILE *archivo_entrada = fopen(argv[1], "r");
        if(!archivo_entrada) {
            printf("no abrio el archivo\n");
            return 1;
        }
        yyin = archivo_entrada; // le digo a flex que lea de aca
    } else {
        printf("te falto el .txt al ejecutar\n");
        return 1;
    }
    
    yyparse();
    return 0;
}
