parser grammar RegoParser;

options { tokenVocab=RegoLexer; } // Tokens to use

/*
 * Parser Rules
 */
 module          : g_package? g_import* policy ;
 g_package       : PACKAGE ref ;
 g_import        : IMPORT ref ( AS var )? ; // Changed IMPORT g_package to IMPORT ref
 policy          : g_rule* ;
 g_rule          : (DEFAULT)? rule_head rule_body* ;
 rule_head       : var (LPAR rule_args RPAR)? (LBRACK term RBRACK)? ((DIFFERENT|UNIFY|ASSIGN) term)? ; // Added ASSIGN
 rule_args       : term ( COMMA term )* ;
 rule_body       : ( ELSE ( UNIFY term )? )? LBRACE NEWLINE* query NEWLINE* RBRACE ;
 query           : literal ( ( SEMICOLON | NEWLINE+ ) literal )* ; // Added + to NEWLINE
 literal         : ( some_decl | expr | NOT expr ) with_modifier* ;
 with_modifier   : WITH term AS term ;
 some_decl       : SOME var ( COMMA var )* ;
 expr            : term | expr_call | expr_infix ;
 expr_call       : var ( DOT var )? LPAR ( term ( COMMA term )* )? RPAR ;
 expr_infix      : ( term UNIFY )? term infix_operator term ;
 term            : ref | var | scalar | array | r_object | r_set | array_compr | object_compr | set_compr ;
 array_compr     : LBRACK term PIPE rule_body RBRACK ;
 set_compr       : LBRACE term PIPE rule_body RBRACE ;
 object_compr    : LBRACE object_item PIPE rule_body RBRACE ;
 infix_operator  : bool_operator | arith_operator | bin_operator | assign_operator | unify_operator ; // Added assign_operator and unify_operator
 bool_operator   : EQUALS | DIFFERENT | INF | SUP | SUP_EQ | INF_EQ ;
 arith_operator  : PLUS | MINUS | TIMES | SLASH ;
 bin_operator    : AMPERSAND | PIPE ;
 assign_operator : ASSIGN ; // Added rule
 unify_operator  : UNIFY ; // Added rule
 ref             : ( var | array | r_object | r_set | array_compr | object_compr | set_compr | expr_call ) ref_arg* ;
 ref_arg         : ref_arg_dot | ref_arg_brack ;
 ref_arg_brack   : LBRACK ( scalar | var | array | r_object | r_set | UNDERSCORE | ref ) RBRACK ; // Added | ref
 ref_arg_dot     : DOT ( var | ref ) ; // Added ref
 var             : VARIABLE | UNDERSCORE ;
 keyword         : (AS | DEFAULT | ELSE | IMPORT | PACKAGE | NOT | WITH | SOME | TRUE | FALSE | NULL) ; // Added rule for keyword in var support
 scalar          : string | NUMBER | TRUE | FALSE | NULL ;
 string          : STRING | raw_string ;
 raw_string      : BACKTICK ( CHAR RAW_STR )* BACKTICK ;
 array           : LBRACK NEWLINE* term ( COMMA NEWLINE* term )* COMMA? NEWLINE* RBRACK ;
 r_object          : LBRACE NEWLINE* object_item (COMMA NEWLINE* object_item )* COMMA? NEWLINE* RBRACE ; // Changed from "'{' object_item ( COMMA object_item )* '}' ;"
 object_item     : ( scalar | ref | var ) COLON NEWLINE* term ;
 r_set             : empty_set | non_empty_set ;
 non_empty_set   : LBRACE NEWLINE* term ( COMMA NEWLINE* term )* COMMA? NEWLINE* RBRACE ;
 empty_set       : SET_OPEN RPAR ;
