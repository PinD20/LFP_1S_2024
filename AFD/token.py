class Token():
    def __init__(self, name, value, line, column):
        self.name = name
        self.value = value
        self.line = line
        self.column = column

    def __str__(self):
        return f"Token({self.name}, {self.value}, {self.line}, {self.column})"