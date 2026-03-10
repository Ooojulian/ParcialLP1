%{
/* julian cristancho - parcial lenguajes */
#include "calc.tab.h"
#include <stdlib.h>
%}

%%

[0-9]+(\.[0-9]+)? { yylval.val = atof(yytext); return NUM; }
"raiz"            { return RAIZ; }
"+"               { return '+'; }
"-"               { return '-'; }
"*"               { return '*'; }
"/"               { return '/'; }
"("               { return '('; }
")"               { return ')'; }
[ \t]             { /* no hacer nada con espacios */ }
\n                { return FIN; }
.                 { return yytext[0]; } /* cualquier otra cosa pasa derecho */

%%

int yywrap() { return 1; }
