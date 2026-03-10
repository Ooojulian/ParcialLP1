grammar Maclaurin;

// regla principal: espera la palabra calcular, dos numeros y fin de linea
inicio: 'calcular' '(' NUM ',' NUM ')' EOF ;

// definicion de tokens basicos
NUM: [0-9]+ ('.' [0-9]+)? ;
WS: [ \t\r\n]+ -> skip ; // ignora espacios y saltos pa q no joda
