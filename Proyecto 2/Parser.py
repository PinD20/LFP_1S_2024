from Token import Token

class Parser():
    def __init__(self, tokens) -> None:
        self.tokens = tokens

        #Controlar fin de tokens
        self.tokens.append(Token("EOF", "EOF", -1, -1))


    def parse(self):
        self.inicio()

    #<inicio> ::= <elemento> <otro_elemento>
    def inicio(self):
        self.elemento()
        self.otro_elemento()

    #<elemento> ::= tk_llaveA <instruccionID> <instruccionER> <instruccionCadenas> tk_llaveC
    def elemento(self):
        if self.tokens[0].name == "tk_llaveA":
            self.tokens.pop(0) #Se extrae el token validado

            self.instruccionID()
            self.instruccionER()
            self.instruccionCadenas()

            if self.tokens[0].name == "tk_llaveC":
                self.tokens.pop(0)
            else:
                print("error, Se esperaba una llave de cierre")
        else:
            print("Error, se esperaba una llave de apertura")