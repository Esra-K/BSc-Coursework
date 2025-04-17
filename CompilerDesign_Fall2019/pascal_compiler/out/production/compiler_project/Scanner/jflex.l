package scanner;

import java.util.Arrays;
import java.io.IOException;
import scanner.Scanner;
import java.util.List;

%%
%class  MyScanner
%implements scanner.Scanner
%function next_token
%unicode
%public
%type  Token


%line
%column


%eofval{
  return null;
%eofval}

%{
    private List<String> tokenTypes;
    public int lineNumber = 1;

    private Token current_token = null;

        public Token CurrentToken() {
            return current_token;
        }

        public Token NextToken() {
            try {
                current_token = next_token();
                return current_token;
            } catch (IOException e) {
                throw new RuntimeException("Unable to get next token", e);
            }
        }



%}

%init{
            tokenTypes = Arrays.asList("array", "assign", "boolean", "break", "begin", "char", "continue",
                        "do", "else", "end", "function", "procedure", "if", "real", "of", "integer", "return",
                        "string", "while", "var", ";", ",", "+", "-", "*", "/", "<", ">", "<=", ">=", "=",
                        "<>", "~", "%", "|", "^", "&", ":=", "(", ")", "[", "]", "false", "true", "and", "or");
%init}



/*patterns*/
digit =                 [0-9]
alpha  =                [A-Za-z]
alpha_num =             ({alpha}|{digit})
hex_digit =             [0-9A-F]
blank =                 Blank

identifier =            {alpha}({alpha_num}|_)*
int =                   {digit}+
hex_integer =           0x{hex_digit}+
real =                  ({int}\.{int}?|\.{int})
char =                  \'[\x20-\x7E]\'
string =                \"[\x20-\x7E]*\"

symbol =                [_*/<>=~%|&\{\}\(\)\[\]]|<=|>=|:=|<>|\+|\,|\;|\^


begin_comment =         <--
end_comment =           -->
content_line_comment =  [^\n]
line_comment =          --~\n
comment =               {begin_comment}~{end_comment}

white_space =           ([\ \r\n\t\f\v]|{comment}|{line_comment}|{blank})
other =                 .

%%

{white_space}    {
                    /* Ignore Whitespace */
                    if(yytext().equals("\n"))
                        lineNumber++;
                    else{

                        String s = yytext();
                        while(s.contains("\n")){
                            lineNumber++;
                            s = s.substring(s.indexOf("\n")+1);
                        }
                    }
                }


{symbol}        {

                    String lexeme = yytext();
                    if(tokenTypes.contains(lexeme))
                        return(new Token<String>(lexeme, lexeme, lineNumber));
                }

{other}         {System.out.println("Invalid syntax found on line " + lineNumber);}

{identifier}    {
                    String lexeme = yytext();
                    // If lexeme found in hashmap, lexeme is a keyword
                    if(tokenTypes.contains(lexeme))
                                if(lexeme.equals("true"))
                                    return(new Token<Boolean>(true, "boolean_constant", lineNumber));
                                else if (lexeme.equals("false"))
                                    return(new Token<Boolean>(false, "boolean_constant", lineNumber));
                                else
                                    return (new Token<String>(lexeme, lexeme, lineNumber));
                    // Otherwise lexeme is an ID
                    return(new Token<String>(lexeme, "id", lineNumber));
                }

{int}           {
                    try {
                        String lexeme = yytext();
                        int num = Integer.parseInt(lexeme);
                        return (new Token<Integer>(num, "integer_constant", lineNumber));
                    }catch (Exception e){
                        System.out.println("error int size");
                    }
                }


{hex_integer}   {
                    try{
                        String lexeme = yytext();
                        int num = Integer.parseInt(lexeme.substring(2), 16);
                        return(new Token<Integer>(num, "integer_constant", lineNumber));
                    }catch (Exception e){
                        System.out.println("error int size");
                    }
                }

{real}          {
                    String lexeme = yytext();
                    float num = Float.parseFloat(lexeme);
                    return(new Token<Float>(num, "real_constant", lineNumber));
                }

{char}          {
                    String lexeme = yytext();
                    char s = lexeme.charAt(1);
                    return(new Token<Byte>((byte)s, "char_constant", lineNumber));
                }


{string}        {
                    String lexeme = yytext();
                    lexeme = lexeme.substring(1,lexeme.length()-1);
                    return(new Token<String>(lexeme, "string_constant", lineNumber));
                }

