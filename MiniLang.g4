grammar MiniLang;
program
    : NEWLINE* statementList EOF
    ;
statementList
    : (statement (NEWLINE+ statement)*)? NEWLINE*
    ;
// Claces de funciones.
statement
    : assign
    | print
    | ifStatement
    | forStatement     
    | expr
    ;

assign
    : ID '=' expr
    ;

print
    : 'print' '(' expr ')'
    ;
// Funcion if
ifStatement
    : 'if' '(' condition ')' '{' NEWLINE* statementList '}' NEWLINE*
    ;
// funcion for 
forStatement
    : 'for' '(' assign ';' condition ';' assign ')' '{' NEWLINE* statementList '}' NEWLINE*
    ;
// condiciones para las funciones.
condition
    : expr op=('>' | '<' | '==' | '!=' | '>=' | '<=') expr
    ;
// operaciones 
expr
    : expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | INT
    | ID
    | '(' expr ')'
    ;
// asignacion de caracteres 
ID : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
NEWLINE : [\r\n]+ ;
WS : [ \t]+ -> skip ;
