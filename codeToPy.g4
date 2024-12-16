grammar codeToPy;

// Reglas de Lexer
HACER : 'hacer' ;
DEFINIR : 'definir' ;
DEVOLVER : 'devolver' ;
MOSTRAR : 'mostrar' ;
SEPARADOR : '--' ;
MUL : '*' ;
PLUS : '+' ;
MOD : '%' ;
DIVIDE : '/' ;
SUB : '-' ;
EXPONENT : '^' ;
SQRT : 'raiz' ;
LPAREN : '(' ;
RPAREN : ')' ;
COLON : ':' ;
COMMA : ',' ;
SI : 'si' ;
SINO : 'sino';
REPETIR : 'repetir' ;
VEZ : 'veces'; 
MENORQUE : '<';
MAYORQUE : '>';
IGUALQUE : '==';
DISTINTOQUE : '!=';
MENORIGUAL : '<=';
MAYORIGUAL : '>=';
Y : 'y';            
O : 'o';  
IGUAL : '=';  
SEMICOLON : ';';   
LBRACE : '{' ;
RBRACE : '}' ;
LBRACKET : '[' ;
RBRACKET: ']' ; 

BOOLEAN : 'true' | 'false';
ID : [a-zA-Z][a-zA-Z0-9_]*; 
STRING : '"' (~["])* '"'; 
NUMERO : [0-9]+; 
FLOAT : [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)?;
WS : [ \t\r\n]+ -> skip; 

COMMENT_SINGLE : '//' ~[\r\n]* -> skip; // Comentarios de una línea
COMMENT_MULTI : '/*' .*? '*/' -> skip; // Comentarios de mas líneas

// Reglas de Parser
inicio : (declaracionFuncion | declaracionVariable | llamadaFuncion | ciclo | condicion | mostrar)* EOF;

declaracionFuncion: HACER ID SEPARADOR (parametros SEPARADOR)? bloque;

parametros : ID (COMMA ID)*;

bloque : LBRACE (instruccion)* RBRACE;

// Instrucciones dentro del bloque
instruccion : ciclo
            | condicion
            | mostrar
            | DEVOLVER expresion SEMICOLON    
            | declaracionVariable
            ;

// Regla para el ciclo
ciclo : REPETIR (ID | NUMERO | expAritmetica) VEZ bloque;

mostrar : MOSTRAR (cadenaConcatenada | ID) SEMICOLON;

// Regla concatenacion
cadenaConcatenada : (STRING | ID) (PLUS(STRING | ID))*;

// Regla para la condición
condicion : SI LPAREN expresion RPAREN bloque (SINO bloque)? ;

declaracionVariable : (DEFINIR)? ID IGUAL (llamadaFuncion | STRING | NUMERO | FLOAT | BOOLEAN | lista | expresion) SEMICOLON;

accesoIndice : ID LBRACKET expresion RBRACKET;

// Regla para expresiones 
expresion : condicionLogica | comparacion | expAritmetica;

expAritmetica : expTermino ((PLUS | SUB | MOD) expTermino)*;

expTermino : expFactor ((MUL | DIVIDE) expFactor)*;

expFactor : expPotencia | expRaiz | (NUMERO | FLOAT | ID | accesoIndice) | LPAREN expAritmetica RPAREN;

expPotencia : expRaiz (EXPONENT expRaiz)+;

expRaiz : SQRT LPAREN expAritmetica RPAREN | (NUMERO | FLOAT) | LPAREN expAritmetica RPAREN;

// Condiciones Logicas
condicionLogica : termino ((Y | O) termino)* ;

// Terminos
termino : comparacion
        | BOOLEAN
        | ID
        | NUMERO
        | FLOAT
        | STRING
        | LPAREN expresion RPAREN
        | lista;

// Reglas comparaciones
comparacion : expAritmetica (MENORQUE | MAYORQUE | IGUALQUE | DISTINTOQUE | MENORIGUAL | MAYORIGUAL) expAritmetica;

// Llamada a una función
llamadaFuncion : ID SEPARADOR (argumento (COMMA argumento)*) SEPARADOR
               | ID SEPARADOR ;

// Regla para argumentos
argumento : NUMERO | STRING | ID;

lista : LBRACKET (expresion (COMMA expresion)*)? RBRACKET ;