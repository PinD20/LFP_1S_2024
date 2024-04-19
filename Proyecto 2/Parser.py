from Token import Token

class Parser():
    def __init__(self, tokens) -> None:
        self.tokens = tokens

        #Controlar fin de tokens
        self.tokens.append(Token("EOF", "EOF", -1, -1))
        #End of file = EOF


    def parse(self):
        self.inicio()

    #<inicio> ::= <elemento> <otro_elemento>
    def inicio(self):
        self.elemento()
        self.otro_elemento()
        print("Análisis sintáctico exitoso")

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

    # <otro_elemento> ::= tk_coma <elemento> <otro_elemento>
    #                  | epsilon
    def otro_elemento(self):
        if self.tokens[0].name == "tk_coma":
            self.tokens.pop(0)
            self.elemento()
            self.otro_elemento()
        else:
            pass #Se acepta épsilon

    #<instruccionID> ::= tk_id tk_dosPuntos tk_entero tk_PyC
    def instruccionID(self):
        if self.tokens[0].name == "tk_id":
            self.tokens.pop(0)
            if self.tokens[0].name == "tk_dosPuntos":
                self.tokens.pop(0)
                if self.tokens[0].name == "tk_entero":
                    self.tokens.pop(0)
                    if self.tokens[0].name == "tk_PyC":
                        self.tokens.pop(0)
                    else:
                        print("Error, se esperaba ';'")
                else:
                    print("Error, se esperaba un entero")
            else:
                print("Error, se esperaba ':'")
        else:
            print("Error, se esperaba la palabra reservada 'ID'")

    #<instruccionER> ::= tk_ER tk_dosPuntos <expresion> <otraExpresion> tk_PyC
    def instruccionER(self):
        if self.tokens[0].name == "tk_ER":
            self.tokens.pop(0)
            if self.tokens[0].name == "tk_dosPuntos":
                self.tokens.pop(0)

                self.expresion()
                self.otraExpresion()

                if self.tokens[0].name == "tk_PyC":
                    self.tokens.pop(0)
                else:
                    print("Error, se esperaba ';' y se obtuvo" + self.tokens[0].name)
            else:
                print("Error, se esperaba ':'")
        else:
            print("Error, se esperaba la palabra reservada 'ER'")

    #<expresion> ::= parA <expresion> parC <operador>
    #              | <elementoER> <operador>
    def expresion(self):
        if self.tokens[0].name == "tk_parA":
            self.tokens.pop(0)

            self.expresion()

            if self.tokens[0].name == "tk_parC":
                self.tokens.pop(0)

                self.operador()
            else:
                print("Error, se esperaba un parentesis de cierre")
        else:
            self.elementoER()
            self.operador()

    #<otraExpresion> ::= <expresion> <otraExpresion>
    #                  | epsilon
    def otraExpresion(self):
        if self.tokens[0].name == "tk_parA" or self.tokens[0].name == "tk_cadena" or self.tokens[0].name == "tk_entero" or self.tokens[0].name == "tk_decimal":
            self.expresion()
            self.otraExpresion()
        else:
            pass #Se acepta épsilon

    #<operador> ::= <operadorUnario>
    #             | tk_Or <expresion>
    #             | epsilon
    def operador(self):
        if self.tokens[0].name == "tk_Mas" or self.tokens[0].name == "tk_Asterisco" or self.tokens[0].name == "tk_Interrogacion":
            self.operadorUnario()
        elif self.tokens[0].name == "tk_Or":
            self.tokens.pop(0)
            self.expresion()
        else:
            pass# Se acepta épsilon

    # <operadorUnario> ::= tk_Mas
    #                    | tk_Asterisco
    #                    | tk_interrogacion
    def operadorUnario(self):
        if self.tokens[0].name == "tk_Mas" or self.tokens[0].name == "tk_Asterisco" or self.tokens[0].name == "tk_Interrogacion":
            self.tokens.pop(0)
        else:
            print("Error, se esperaba un operador unario")

    # <elementoER> ::= tk_cadena
    #                | tk_entero
    #                | tk_decimal
    def elementoER(self):
        if self.tokens[0].name == "tk_cadena" or self.tokens[0].name == "tk_entero" or self.tokens[0].name == "tk_decimal":
            self.tokens.pop(0)
        else:
            print("Error, se esperaba cadena, entero o decimal")

    #<instruccionCadenas> ::= tk_Cadenas tk_dosPuntos tk_cadena <otraCadena> tk_PyC
    def instruccionCadenas(self):
        if self.tokens[0].name == "tk_Cadenas":
            self.tokens.pop(0)
            if self.tokens[0].name == "tk_dosPuntos":
                self.tokens.pop(0)
                if self.tokens[0].name == "tk_cadena":
                    self.tokens.pop(0)

                    self.otraCadena()

                    if self.tokens[0].name == "tk_PyC":
                        self.tokens.pop(0)
                    else:
                        print("Error, se esperaba ';' y se obtuvo " + self.tokens[0].name)
                else:
                    print("Error, se esperaba una cadena")
            else:
                print("Error, se esperaba ':'")
        else:
            print("Error, se esperaba la palabra reservada 'Cadenas'")

    # <otraCadena> ::= tk_coma tk_cadena <otraCadena>
    #                | epsilon
    def otraCadena(self):
        if self.tokens[0].name == "tk_coma":
            self.tokens.pop(0)
            if self.tokens[0].name == "tk_cadena":
                self.tokens.pop(0)
                self.otraCadena()
            else:
                print("Error, se esperaba una cadena y se obtuvo" + self.tokens[0].name)
        else:
            pass #Se acepta épsilon