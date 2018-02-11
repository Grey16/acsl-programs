/*
    determine which symbol is missing
    determine if it's a left or right
    if right
        Go past all left brackets + lower symbols (Ex ')' is lower than ']') 
        LOOP
            Record index in an ArrayList
            Go right to another place
    if left
        Go past all higher symbols (Ex '{' is higher than '[')
        LOOP
            Record index in ArrayList
            Go right to another place until a lower symbol is reached
    SINGLE INTEGERS ARE NEVER ENCLOSED!
   
Assume { is missing
    Normal case: [()]}
        60+[15*(520-505)]/5-23}
            "1" {60+[15*(520-505)]/5-23}
            "4" 60+{[15*(520-505)]/5-23}
            "19" 60+[15*(520-505)]/{5-23}
    Other case: }[()]
        60+70+6}*[5-4*(3+3)]
        "1" {60+70+6}*[5-4*(3+3)]
        "4" 60+{70+6}*[5-4*(3+3)]
        
Assume } is missing
    Normal case: {[()]
        Test input#3
    Other case: [()]{
        [34*12+(39-38)]+60*{29-19+69
        "26" [34*12+(39-38)]+60*{29-19}+69
        "29" [34*12+(39-38)]+60*{29-19+69}

Assume [ is missing
    Normal case: {()]}
        Test input#4
    Other case: {]()}
        {60+38+9}*60+29*20]-60+(302-10)
        
Assume ] is missing
    Normal case: {[()}
        Test input#1
    Other case: {()[}
        {32*510+(8/4)*[2+13-35/26}
        "20" {32*510+(8/4)*[2+13]-35/26}
        "23" {32*510+(8/4)*[2+13-35]/26}
        "26" {32*510+(8/4)*[2+13-35/26]}
Assume ( is missing
    Normal case: {[)]}
        Test input#2
    Other case: {)[]}
Assume ) is missing
    Normal case: Test input#5
    Other case: {([]}
        {32*410+(8/4*[2+34]/23}
        "13" {32*410+(8/4)*[2+34]/23}
        
Edge case: {302-343}+(34-3)+[349-334
Edge case: 39393-30]+{39-20+(203-20)}
*/
public class Enclosure {
    public static void main(String[] args) {
    }    
}    
