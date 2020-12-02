lexer grammar RegoLexer;
/*
 * Lexer Rules
 */

 // Fragments for keywords
fragment A          : ('A'|'a') ;
fragment S          : ('S'|'s') ;
fragment D          : ('D'|'d') ;
fragment E          : ('E'|'e') ;
fragment F          : ('F'|'f') ;
fragment U          : ('U'|'u') ;
fragment L          : ('L'|'l') ;
fragment T          : ('T'|'t') ;
fragment I          : ('I'|'i') ;
fragment M          : ('M'|'m') ;
fragment P          : ('P'|'p') ;
fragment O          : ('O'|'o') ;
fragment R          : ('R'|'r') ;
fragment C          : ('C'|'c') ;
fragment K          : ('K'|'k') ;
fragment G          : ('G'|'g') ;
fragment N          : ('N'|'n') ;
fragment W          : ('W'|'w') ;
fragment H          : ('H'|'h') ;

fragment CR         : '\r' ;
fragment LF         : '\n' ;

fragment ALPHA      : ([a-zA-Z]) ;
fragment DIGIT      : [0-9] ;

// Tokenize new line in this mode
LBRACE              : '{' -> pushMode(PARSENEWLINE) ;

// Explicit tokens for non-combined grammar
LPAR                : '(' ;
RPAR                : ')' ;
LBRACK              : '[' ;
RBRACK              : ']' ;
ASSIGN              : ':=' ;
UNIFY               : '=' ;
COMMA               : ',' ;
SEMICOLON           : ';' ;
DOT                 : '.' ;
PIPE                : '|' ;
EQUALS              : '==' ;
DIFFERENT           : '!=' ;
INF                 : '<' ;
SUP                 : '>' ;
INF_EQ              : '<=' ;
SUP_EQ              : '>=' ;
PLUS                : '+' ;
MINUS               : '-' ;
TIMES               : '*' ;
SLASH               : '/' ;
AMPERSAND           : '&' ;
UNDERSCORE          : '_' ;
BACKTICK            : '`' ;
COLON               : ':' ;
SET_OPEN            : 'set(' ;
RAW_STR             : '-`' ;

// Tokens
AS                  : A S ;
DEFAULT             : D E F A U L T ;
ELSE                : E L S E ;
IMPORT              : I M P O R T ;
PACKAGE             : P A C K A G E ;
NOT                 : N O T ;
WITH                : W I T H ;
SOME                : S O M E ;
TRUE                : T R U E ;
FALSE               : F A L S E ;
NULL                : N U L L ;
NEWLINE             : (CR? LF | CR)+ -> skip ;
COMMENT             : '#' .*? CR? LF -> skip ;
STRING              : '"' ~["]* '"' ;
NUMBER              : '-'?('0'|[1-9][0-9]*)('.'[0-9]+)?([eE][+-]?[0-9]+)? ;
VARIABLE            : ( ALPHA | UNDERSCORE ) ( ALPHA | DIGIT | UNDERSCORE )* ; // Added from var grammar rule
WHITESPACE          : (' ' | '\t')+ -> skip ;
CHAR                : [\u0000-\u007F] ;
ANY                 : . ; // This should not be matched


// Mode to parse newlines
mode PARSENEWLINE;

RBRACE              : '}' -> popMode ;


// Explicit tokens for non-combined grammar
P_LBRACE              : '{' -> type(LBRACE), pushMode(PARSENEWLINE) ; // Added for braces inside braces
P_LPAR                : '(' -> type(LPAR) ;
P_RPAR                : ')' -> type(RPAR) ;
P_LBRACK              : '[' -> type(LBRACK) ;
P_RBRACK              : ']' -> type(RBRACK) ;
P_ASSIGN              : ':=' -> type(ASSIGN) ;
P_UNIFY               : '=' -> type(UNIFY) ;
P_COMMA               : ',' -> type(COMMA) ;
P_SEMICOLON           : ';' -> type(SEMICOLON) ;
P_DOT                 : '.' -> type(DOT) ;
P_PIPE                : '|' -> type(PIPE) ;
P_EQUALS              : '==' -> type(EQUALS) ;
P_DIFFERENT           : '!=' -> type(DIFFERENT) ;
P_INF                 : '<' -> type(INF) ;
P_SUP                 : '>' -> type(SUP) ;
P_INF_EQ              : '<=' -> type(INF_EQ) ;
P_SUP_EQ              : '>=' -> type(SUP_EQ) ;
P_PLUS                : '+' -> type(PLUS) ;
P_MINUS               : '-' -> type(MINUS) ;
P_TIMES               : '*' -> type(TIMES) ;
P_SLASH               : '/' -> type(SLASH) ;
P_AMPERSAND           : '&' -> type(AMPERSAND) ;
P_UNDERSCORE          : '_' -> type(UNDERSCORE) ;
P_BACKTICK            : '`' -> type(BACKTICK) ;
P_COLON               : ':' -> type(COLON) ;
P_SET_OPEN            : 'set(' -> type(SET_OPEN) ;
P_RAW_STR             : '-`' -> type(RAW_STR) ;

// Tokens
P_AS                  : A S -> type(AS) ;
P_DEFAULT             : D E F A U L T -> type(DEFAULT) ;
P_ELSE                : E L S E -> type(ELSE) ;
P_IMPORT              : I M P O R T -> type(IMPORT) ;
P_PACKAGE             : P A C K A G E -> type(PACKAGE) ;
P_NOT                 : N O T -> type(NOT) ;
P_WITH                : W I T H -> type(WITH) ;
P_SOME                : S O M E -> type(SOME) ;
P_TRUE                : T R U E -> type(TRUE) ;
P_FALSE               : F A L S E -> type(FALSE) ;
P_NULL                : N U L L -> type(NULL) ;
P_NEWLINE             : (CR? LF | CR)+ -> type(NEWLINE) ;
P_COMMENT             : '#' .*? CR? LF -> skip ;
P_STRING              : '"' ~["]* '"' -> type(STRING) ;
P_NUMBER              : '-'?('0'|[1-9][0-9]*)('.'[0-9]+)?([eE][+-]?[0-9]+)? -> type(NUMBER) ;
P_VARIABLE            : ( ALPHA | UNDERSCORE ) ( ALPHA | DIGIT | UNDERSCORE )* -> type(VARIABLE) ; // Added from var grammar rule
P_WHITESPACE          : (' ' | '\t')+ -> skip ;
P_CHAR                : [\u0000-\u007F] -> type(CHAR) ;
P_ANY                 : . -> type(ANY) ; // This should not be matched
