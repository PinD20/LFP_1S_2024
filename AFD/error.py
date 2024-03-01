class Error():
    def __init__(self, lexema, errorChar, type, line, column):
        self.lexema = lexema
        self.errorChar = errorChar
        self.type = type
        self.line = line
        self.column = column

    def __str__(self):
        return f"Error({self.lexema}, {self.errorChar}, {self.type}, {self.line}, {self.column})"