from Parser import Parser
from Token import Token

'''
============= Entrada =================

{
    ID: 1;
    ER: "abc"*(8|20)?1;
    CADENAS: "abc201", "81";
}

'''

def llenarLista():
    tokens = []
    tokens.append(Token("tk_llaveA", "{", 1, 1))
    tokens.append(Token("tk_id", "ID", 1, 1))
    tokens.append(Token("tk_dosPuntos", ":", 1, 1))
    tokens.append(Token("tk_cadena", "\"hola\"", 1, 1))
    tokens.append(Token("tk_cadena", "\"hola\"", 1, 1))
    tokens.append(Token("tk_cadena", "\"hola\"", 1, 1))
    tokens.append(Token("tk_cadena", "\"hola\"", 1, 1))
    tokens.append(Token("tk_cadena", "\"hola\"", 1, 1))
    tokens.append(Token("tk_cadena", "\"hola\"", 1, 1))
    tokens.append(Token("tk_cadena", "\"hola\"", 1, 1))
    tokens.append(Token("tk_cadena", "\"hola\"", 1, 1))
    
    #tokens.append(Token("tk_entero", "1", 1, 1))
    tokens.append(Token("tk_PyC", ";", 1, 1))
    tokens.append(Token("tk_ER", "ER", 1, 1))
    tokens.append(Token("tk_dosPuntos", ":", 1, 1))
    tokens.append(Token("tk_cadena", "\"abc\"", 1, 1))
    tokens.append(Token("tk_Asterisco", "*", 1, 1))
    tokens.append(Token("tk_parA", "(", 1, 1))
    tokens.append(Token("tk_entero", "8", 1, 1))
    tokens.append(Token("tk_Or", "|", 1, 1))
    tokens.append(Token("tk_entero", "20", 1, 1))
    tokens.append(Token("tk_parC", ")", 1, 1))
    tokens.append(Token("tk_Interrogacion", "?", 1, 1))
    tokens.append(Token("tk_entero", "1", 1, 1))
    tokens.append(Token("tk_PyC", ";", 1, 1))
    tokens.append(Token("tk_Cadenas", "CADENAS", 1, 1))
    tokens.append(Token("tk_dosPuntos", ":", 1, 1))
    tokens.append(Token("tk_cadena", "\"abc201\"", 1, 1))
    tokens.append(Token("tk_coma", ",", 1, 1))
    tokens.append(Token("tk_cadena", "\"81\"", 1, 1))
    tokens.append(Token("tk_PyC", ";", 1, 1))
    tokens.append(Token("tk_llaveC", "}", 1, 1))

    return tokens

if __name__ == "__main__":
    #Se crea el objeto parser
    parser = Parser(llenarLista())
    
    #Se llama al método parse
    parser.parse()