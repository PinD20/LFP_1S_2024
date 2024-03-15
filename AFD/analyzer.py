from token import Token
from error import Error

class Analyzer():
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.errors = []

    def isValidSymbol(self, char):
        return char in [":", "{", "}", ";", ",", "[", "]"]
    
    def state0(self, char, line, column, lexema):
        if self.isValidSymbol(char):
            return 10
        elif char == '"':
            return 1
        elif char.isalpha():
            return 2
        else:
            #Omitir espacios, tabulaciones y saltos de línea
            if ord(char) == 10 or ord(char) == 32 or ord(char) == 9:
                pass
            else:# Es un error
                self.errors.append(Error(lexema, char, "Léxico", line, column))
            return 0

    def analyze(self):
        line = 1
        column = 1
        lexema = ""

        state = 0
        previousState = -1
        self.tokens.clear()
        self.errors.clear()

        for char in self.text:
            if state == 0:
                state = self.state0(char, line, column, lexema)
                if state == 0:
                    #Se reinicia el lexema
                    lexema = ""
                    previousState = -1
                elif state == 10:
                    lexema += char
                    previousState = 0
                    self.tokens.append(Token("Signo", lexema, line, column))
                    state = 0
                    lexema = ""
                else:
                    lexema += char
                    previousState = 0

            
            elif state == 1:
                if char == '"':
                    lexema += char
                    state = 10
                    previousState = 1
                elif char != "\n":
                    lexema += char
                    state = 1
                else:#Error
                    self.errors.append(Error(lexema, char, "Léxico", line, column))

                    #Se reinicia el lexema
                    lexema = ""
                    state = 0
            
            elif state == 2:
                if char.isalpha():
                    lexema += char
                    state = 2
                else: #Es un estado de aceptación, se guarda el token
                    self.tokens.append(Token("Palabra Reservada", lexema, line, column - len(lexema)))

                    #Se reinicia el lexema
                    lexema = ""
                    state = 0

                    #Actúa como si estuviera en el estado 0 de nuevo
                    state = self.state0(char, line, column, lexema)
                    if state == 0:
                        #Se reinicia el lexema
                        lexema = ""
                        previousState = -1
                    else:
                        lexema += char
                        previousState = 0

            elif state == 10:
                if previousState == 0:
                    self.tokens.append(Token("Signo", lexema, line, column - len(lexema)))
                elif previousState == 1:
                    self.tokens.append(Token("String", lexema, line, column - len(lexema)))
                
                lexema = "" #Se limpia el lexema porque ya fue almacenado

                state = self.state0(char, line, column, lexema)
                if state == 0:
                    #Se reinicia el lexema
                    lexema = ""
                    previousState = -1
                else:
                    lexema += char
                    previousState = 0


            # Control de líneas y columnas
            
            #Salto de línea
            if ord(char) == 10:
                line += 1
                column = 1
            #Tabulación
            elif ord(char) == 9:
                column += 4

            #Espacio
            elif ord(char) == 32:
                column += 1

            else:
                column += 1