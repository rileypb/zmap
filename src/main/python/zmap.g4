
grammar zmap;

@header {
from map import *
}

parse
    : ifmaps EOF
    ;

ifmaps
    : ifmapblock+
    ;

ifmapblock
    : name LBRACE ifmap RBRACE (NL+ EOF? | EOF)
    ;

ifmap
    : (passage | comment | NL)+
    ;

passage
    : node directed_arrow (node | unknown) (modifier)? (NL | EOF)
    ; 

comment
    : '#' ~(NL)* (NL | EOF)
    ;

node
    : special? (room | freeRoom)
    ;

room
    : LBRACK name RBRACK
    ; 

freeRoom
    : LPAREN name RPAREN
    ;

modifier
    : CLOSE
    | FAR
    ;


name
    : NAME
    ;

directed_arrow
    : left_direction larrow 
    | left_direction barrow right_direction?
    | barrow right_direction
    | rarrow right_direction
    ;

larrow
    : LARROW
    ;

rarrow
    : RARROW
    ;

barrow
    : BARROW
    ;

left_direction
    : DIRECTION
    ;

right_direction
    : DIRECTION
    ;

arrow
    : LARROW | RARROW | BARROW
    ;


unknown
    : QUESTION
    ;


special
    : STAR
    ;


LPAREN
    : '('
    ;


RPAREN
    : ')'
    ;


NL
    : '\n'
    ;

DIRECTION
    : N
    | NE
    | E
    | SE
    | S
    | SW
    | W
    | NW
    | U
    | D
    ;

NAME
    : ALPHA (ALPHANUM)*
    ;

LBRACE
    : '{'
    ;

RBRACE
    : '}'
    ;

QUESTION
    : '?'
    ;


STAR
    : '*'
    ;


LARROW
    : '-->'
    ;


RARROW
    : '<--'
    ;


BARROW
    : '<->'
    ;


LBRACK
    : '['
    ;


RBRACK
    : ']'
    ;


N
    : 'n'
    ;


NE
    : 'ne'
    ;


E
    : 'e'
    ;


SE
    : 'se'
    ;


S
    : 's'
    ;


SW
    : 'sw'
    ;


W
    : 'w'
    ;


NW  
    : 'nw'  
    ;

U
    : 'u'
    ;
    
D
    : 'd'
    ;
    
CLOSE
    : '<'
    ;

FAR
    : '>'
    ;

fragment ALPHA
   : ('a' .. 'z') | ('A' .. 'Z')
   ;
 
fragment ALPHANUM
    : ALPHA | ('0' .. '9') | ' ' | '_'
    ;

