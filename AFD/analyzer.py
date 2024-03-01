class Analyzer():
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.errors = []

    def analyze(self):
        line = 1
        column = 1
        lexema = ""

        state = 0
        self.tokens.clear()
        self.errors.clear()

        for char in self.text:
            #Inicia análisis del AFD
            pass


