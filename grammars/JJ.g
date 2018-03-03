// start rule
start:         (NEWLINE | token)+                               ;

// Rules
@token:         definition | expr | import_stmt | assign_stmt                              ;

// controllare sulla grammatica di python come è implementato
definition:     DEF name param* COLON body                             ;
body:           (NEWLINE INDENT (expr | NEWLINE)+ DEDENT) | (expr)+                              ;
param: name+;

import_stmt:    IMPORT name (COMMA name)?                      ;
assign_stmt:    assign_normal | assign_drop | assign_acc  | assign_acc_drop                        ;
assign_normal:  IMPLY (name | (LPAR name+ RPAR));
assign_drop:    DROP_IMPLY (name | (LPAR name+ RPAR));
assign_acc:     ACC name;
assign_acc_drop:DROP_ACC name;
@expr:          atom | assign_stmt | LPAR expr RPAR                          ;

@atom:          name | number | string | list | array | bool               ;
bool:           TRUE | FALSE;
name:           NAME | PUNT;
@number:        int | float                                     ;

int:            '[0-9]\d*'                                      ;
float:          '(\d+\.\d*|\.\d+)'                              ;

//List
list:           n_list | emptylist                              ;
emptylist:      LSQB RSQB                                       ;
@n_list:        LSQB (expr)+ RSQB                               ;

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
            '|' UNDERSCORE
            ']+'
(%unless
    IMPLY:      '->'    ;
    DROP_IMPLY:     '>->'    ;
    ACC:        '=>';
    DROP_ACC:   '>=>';
)                ;

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
PERCENT:    '\%'    ;
UNDERSCORE: '_'     ;




// da qui in poi è copiato dalla grammatica di python
NEWLINE:
    '(\r?\n[\t ]*)+'    (%newline);
WS:
    '[\t \f,]+'          (%ignore);
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

TRUE:           'True';
FALSE:          'False';
);



// INDENTING AND DEDENTING
EOF: '<EOF>';

INDENT: '<INDENT>';
DEDENT: '<DEDENT>';


###
from plyplus.grammars.python_indent_postlex import PythonIndentTracker
self.lexer_postproc = PythonIndentTracker
