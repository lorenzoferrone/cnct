// start rule
start:         (NEWLINE | token)+                               ;

// Rules
@token:         definition | expr | import_stmt | assign_stmt                              ;

// controllare sulla grammatica di python come è implementato
definition:     DEF name param* COLON body                             ;
body:           (NEWLINE INDENT (expr | NEWLINE)+ DEDENT) | (expr)+                              ;
param: name+;

import_stmt:    IMPORT name (COMMA name)?                     ;
assign_stmt:    assign_normal | assign_drop | assign_acc  | assign_acc_drop                        ;
assign_normal:  IMPLY (name | (LPAR name+ RPAR));
assign_drop:    DROP_IMPLY (name | (LPAR name+ RPAR));
assign_acc:     ACC name;
assign_acc_drop:DROP_ACC name;
@expr:          atom | assign_stmt                          ;

@atom:          number | name | string | list | array | concat | bool               ;
bool:           TRUE | FALSE;
@number:        int | float                                ;
name:           NAME | PUNT;

int:            '\-?[0-9]\d*'                                      ;
float:          '\-?(\d+\.\d*|\.\d+)'                              ;

//List
list:           n_list | emptylist                              ;
emptylist:      LSQB RSQB                                       ;
@n_list:        LSQB (expr)+ RSQB                               ;

// array
array:          LPAR (atom)+ RPAR                                ;

// parallel_execution
concat:         LBRACE atom+ RBRACE                           ;
// atoms:          atom+;

string:         STRING  ;
%fragment       STRING_INTERNAL: '.*?(?<!\\)(\\\\)*?' ;
%fragment       QUOTE: '\'';
%fragment       DBLQUOTE: '"';

STRING :    '(' DBLQUOTE '(?!"")' STRING_INTERNAL DBLQUOTE
            '|' QUOTE '(?!\'\')' STRING_INTERNAL QUOTE
            ')' ;




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
            '|' EXP
            ']+'
(%unless
    IMPLY:      '->'        ;
    DROP_IMPLY: '>->'       ;
    ACC:        '=>'        ;
    DROP_ACC:   '>=>'       ;
)                           ;

STAR:       '\*'    ;
SLASH:      '/'     ;
PLUS:       '\+'    ;
DBLPLUS:    '\+\+'  ;
DBLSTAR:    '\*\*'  ;
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
RSQB:       '\]'    ;
LBRACE:     '\{'    ;
RBRACE:     '\}'    ;
COMMA:      ','     ;
DOT:        '\.'    ;
EXP:        '\^'    ;
LPAR:       '\('    ;
RPAR:       '\)'    ;
SEMI:       '\;'    ;
AT:         '@'     ;
PERCENT:    '\%'    ;
UNDERSCORE: '_'     ;
MINUS:      '\-'    ;




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
IMPORT:     'import'    ;
DEF:        'def'       ;
TRUE:       'True'      ;
FALSE:      'False'     ;
);


// INDENTING AND DEDENTING
EOF: '<EOF>';

INDENT: '<INDENT>';
DEDENT: '<DEDENT>';


###
from plyplus.grammars.python_indent_postlex import PythonIndentTracker
self.lexer_postproc = PythonIndentTracker
