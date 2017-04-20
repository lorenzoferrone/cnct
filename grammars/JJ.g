// start rule
start:         (NEWLINE | token)+                               ;

// Rules
@token:         definition | expr | import_stmt | assign_stmt                              ;

// controllare sulla grammatica di python come è implementato
definition:     DEF name COLON body                             ;
body:           (NEWLINE INDENT (expr | assign_stmt | NEWLINE)+ DEDENT) | (expr | assign_stmt)+                              ;

import_stmt:    IMPORT name (COMMA name)?                      ;
assign_stmt:    COLON COLON name                               ;
@expr:          atom | LPAR expr RPAR                          ;

@atom:          name | number | string | list | array | bool                 ;
bool:           TRUE | FALSE;
TRUE:           'True';
FALSE:          'False';
name:           NAME | PUNT                                          ;
@number:        int | float                                     ;

int:            '[0-9]\d*'                                      ;
float:          '(\d+\.\d*|\.\d+)'                              ;

//List
list:           n_list | emptylist                              ;
emptylist:      LSQB RSQB                                       ;
@n_list:        LSQB (atom)+ RSQB                               ;

// array
array:          LPAR (atom)+ RPAR                                ;

string:         STRING  ;
%fragment       STRING_INTERNAL: '.*?(?<!\\)(\\\\)*?' ;
%fragment       QUOTE: '\'';
%fragment       DBLQUOTE: '"';

STRING :    '(' DBLQUOTE '(?!"")' STRING_INTERNAL DBLQUOTE
            '|' QUOTE '(?!\'\')' STRING_INTERNAL QUOTE
            ')' ;


// SECTION: punctuation and math symbols
// @punt:       '[\+\-]+'                          ;
// @punt:       (PLUS | MINUS)+                        ;

PUNT:       '[' PLUS
            '|' MINUS
            '|' STAR
            '|' EQUAL
            '|' LESS
            '|' GREATER
            '|' EXCL
            '|' AT
            '|' SLASH
            '|' PERCENT
            '|' DOT
            ']+'                 ;

STAR:       '\*'    ;
SLASH:      '/'     ;
PLUS:       '\+'    ;
DBLPLUS:    '\+\+'  ;
DBLSTAR:    '\*\*'  ;
MINUS:      '\-'     ;
EQUAL:      '='     ;
COLON:      ':'     ;
EXCL:       '!'     ;
DBLEQUAL:   '=='    ;
NEQ:        '!='    ;
LESS:       '<'     ;
GREATER:    '>'     ;
LEQ:        '<='    ;
GEQ:        '>='    ;
LSQB:       '\['    ;
RSQB:       '\]'     ;
COMMA:      ','     ;
DOT:        '\.'    ;
EXP:        '\^'     ;
LPAR:       '\('    ;
RPAR:       '\)'    ;
SEMI:       '\;'    ;
AT:         '@'     ;
IMPLY:      '->'    ;
PERCENT:    '\%'    ;




// da qui in poi è copiato dalla grammatica di python
NEWLINE:
    '(\r?\n[\t ]*)+'    (%newline);
WS:
    '[\t \f]+'          (%ignore);
LINE_CONT:
    '\\[\t \f]*\r?\n'   (%ignore) (%newline);
COMMENT:
    '\#[^\n]*'          (%ignore);






// SECTION: VARIABLE NAMES AND KEYWORDS
NAME:       '[A-Za-z][\w.\?]*(?!r?"|r?\')'// Match names and not strings (r"...")

(%unless
IMPORT:     'import';
PRINT:      'P';
DEL:        'Del';
AS:         'As';
LAMBDA:     'Lambda';
LOOP:       'Loop';
DO:         'Do';
BY:         'By';
CASE:       'K';
// Definitions
DEF:        'def';

// Flow Blocks
IF:         '\?';
FOR:        'For';
WHILE:      'While';

// Flow
BREAK:      'Break';
CONTINUE:   'Continue';
RETURN:     'Return';
YIELD:      'Yield';

// Operators
AND:        'And';
OR:         'Or';
NOT:        'Not';
IS:         'Is';
IN:         'In';
XOR:        'Xor';
);



// INDENTING AND DEDENTING
EOF: '<EOF>';

INDENT: '<INDENT>';
DEDENT: '<DEDENT>';


###
from plyplus.grammars.python_indent_postlex import PythonIndentTracker
self.lexer_postproc = PythonIndentTracker
