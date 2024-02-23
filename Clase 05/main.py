import graphviz

from graphviz import Source

#PRIMERA FORMA DE CREAR EL GRAFO
#Crear el grafo
dot = graphviz.Digraph(comment='The Round Table')

#Agregar nodos
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('C', 'Sir Lancelot the Brave')

#Agregar conexiones
dot.edges(['AB', 'AC'])

#Agregar 1 conexión
dot.edge('B', 'L')

#Imprimir el código DOT
#print(dot.source)

#Crear imagen en PDF
dot.render('imagen.svg').replace('\\', '/')

#SEGUNDA FORMA DE CREAR EL GRAFO
codigoDot = '''
digraph {
    A [label="King Arthur 2"]
    B [label="Sir Bedevere the Wise"]
    C [label="Sir Lancelot the Brave"]
    A -> B
    A -> C
    B -> L [constraint=true]
}
'''

#1 forma
source = Source(codigoDot, filename="imagen", format="svg")
#Abrir la imagen
source.view()


#2 forma
source = Source(codigoDot, filename="codigo.gv")
source.render(format="svg")
source.render(format="pdf")
source.render(format="png")
source.render(format="jpg")
