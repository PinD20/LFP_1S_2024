from analyzer import Analyzer

if __name__ == "__main__":
    archivo = open("entrada.txt", "r", encoding="utf-8")
    text = archivo.read()
    
    #Instanciando analizador
    analyzer = Analyzer(text)
    analyzer.analyze()


    for token in analyzer.tokens:
        print(token)
    for error in analyzer.errors:
        print(error)
