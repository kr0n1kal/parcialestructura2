#CLASE QUE REPRESENTA UN NODO EN UN ARBOL BINARIO. CADA NODO TIENE UN VALOR Y REFERENCIAS A SUS NODOS HIJOS IZQUIERDO Y DERECHO
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

#FUNCION QUE CREA UN ARBOL BINARIO BASICO DE PREGUNTAS Y RESPUESTAS
def construir_arbol():
    raiz = Nodo("¿Es un animal?")
    raiz.izquierda = Nodo("¿Es un objeto?")
    raiz.derecha = Nodo("¿Es un personaje?")

    raiz.izquierda.izquierda = Nodo("¿Se puede comer?")
    raiz.izquierda.derecha = Nodo("¿Es grande?")
    raiz.derecha.izquierda = Nodo("¿Es real?")
    raiz.derecha.derecha = Nodo("¿Es de ficción?")

    return raiz

#FUNCION PRINCIPAL DEL JUEGO. RECIBE UN NODO COMO ENTRADA Y GUIA AL JUGADOR A TRAVES DEL ARBOL DE PREGUNTAS Y RESPUESTAS HASTA LLEGAR A UNA HOJA
#SI EL PROGRAMA ADIVINA CORRECTAMENTE, FELICITA AL JUGADOR Y APRENDE SI LA RESPUESTA ES INCORRECTA
#SI LA ADIVINANZA ES INCORRECTA, EL PROGRAMA PIDE AL JUGADOR UNA NUEVA PREGUNTA PARA DISTINGUIR EL OBJETO/ANIMAL/PERSONAJE DE LA ADIVINANZA ANTERIOR Y ACTUALIZA EL ARBOL
def jugar_adivinanza(nodo):
    if nodo.izquierda is None and nodo.derecha is None:
        respuesta = input("¿Es un(a) " + nodo.valor + "? ")
        if respuesta.lower() == "si":
            print("¡Genial! He adivinado correctamente.")
        else:
            print("¡Oh no! Parece que necesito mejorar mis habilidades de adivinación.")
            objeto = input("¿Qué era el objeto/animal/personaje que pensabas? ")
            pregunta = input("Ingrese una pregunta que distinga un(a) " + nodo.valor + " de un(a) " + objeto + ": ")
            respuesta_nueva = input("¿Cuál es la respuesta para un(a) " + nodo.valor + " en esa pregunta? (si/no) ")
            nodo.valor = pregunta
            if respuesta_nueva.lower() == "si":
                nodo.izquierda = Nodo(nodo.valor)
                nodo.derecha = Nodo(objeto)
            else:
                nodo.izquierda = Nodo(objeto)
                nodo.derecha = Nodo(nodo.valor)
        return

    respuesta = input(nodo.valor + " ")
    if respuesta.lower() == "si":
        jugar_adivinanza(nodo.izquierda)
    elif respuesta.lower() == "no":
        jugar_adivinanza(nodo.derecha)
    else:
        print("Respuesta no válida. Por favor, responde 'si' o 'no'.")
        jugar_adivinanza(nodo)

#FUNCION QUE EXPORTA EL ARBOL A UN ARCHIVO EXTERNO EN FORMATO DE TEXTO
#INCLUYE LAS NOTACIONES PREORDER, INORDER Y POSTORDER DEL ARBOL
def exportar_arbol(arbol, archivo):
    with open(archivo, "w") as f:
        f.write("Preorder: " + preorder(arbol) + "\n")
        f.write("Inorder: " + inorder(arbol) + "\n")
        f.write("Postorder: " + postorder(arbol) + "\n")

#FUNCIONES AUXILIARES PARA OBTENER LAS NOTACIONES PREORDER
def preorder(nodo):
    if nodo is None:
        return ""
    return nodo.valor + " " + preorder(nodo.izquierda) + preorder(nodo.derecha)

#FUNCIONES AUXILIARES PARA OBTENER LAS NOTACIONES INORDER
def inorder(nodo):
    if nodo is None:
        return ""
    return inorder(nodo.izquierda) + nodo.valor + " " + inorder(nodo.derecha)

#FUNCIONES AUXILIARES PARA OBTENER LAS NOTACIONES POSTORDER
def postorder(nodo):
    if nodo is None:
        return ""
    return postorder(nodo.izquierda) + postorder(nodo.derecha) + nodo.valor + " "

#FUNCION QUE IMPORTA UN ARBOL DESDE UN ARCHIVO EXTERNO
#LEE LAS NOTACIONES PREORDER, INORDER Y POSTORDER DEL ARCHIVO Y RECONSTRUYE EL ARBOL
def importar_arbol(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        preorder_str = lineas[0].split(": ")[1].strip()
        inorder_str = lineas[1].split(": ")[1].strip()
        postorder_str = lineas[2].split(": ")[1].strip()

    raiz = reconstruir_arbol(preorder_str.split(), inorder_str.split(), postorder_str.split())
    return raiz

#FUNCION AUXILIAR QUE RECONSTRUYE EL ARBOL A PARTIR DE LAS NOTACIONES PREORDER, INORDER Y POSTORDER
def reconstruir_arbol(preorder, inorder, postorder):
    if not preorder:
        return None
    valor = preorder[0]
    nodo = Nodo(valor)
    if len(preorder) == 1:
        return nodo
    index = inorder.index(valor)
    nodo.izquierda = reconstruir_arbol(preorder[1:index + 1], inorder[:index], postorder[:index])
    nodo.derecha = reconstruir_arbol(preorder[index + 1:], inorder[index + 1:], postorder[index:-1])
    return nodo

#FUNCION PRINCIPAL QUE INICIA EL JUEGO
#GUIA AL JUGADOR A TRAVES DEL JUEGO DE ADIVINANZAS Y PROPORCIONA OPCIONES PARA EXPORTAR E IMPORTAR EL ARBOL
def main():
    print("Bienvenido al juego de adivinanzas.")
    print("Piensa en un objeto, animal o personaje y responde las preguntas con 'si' o 'no'.")

    arbol = construir_arbol()
    jugar_adivinanza(arbol)

    opcion_exportar = input("¿Quieres exportar el árbol a un archivo? (si/no) ")
    if opcion_exportar.lower() == "si":
        archivo_salida = input("Ingrese el nombre del archivo de salida: ")
        exportar_arbol(arbol, archivo_salida)
        print("El árbol ha sido exportado exitosamente.")

    opcion_importar = input("¿Quieres importar un árbol desde un archivo? (si/no) ")
    if opcion_importar.lower() == "si":
        archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
        arbol_importado = importar_arbol(archivo_entrada)
        print("El árbol ha sido importado exitosamente.")
        print("Continuemos jugando con el árbol importado.")
        jugar_adivinanza(arbol_importado)

if __name__ == "__main__":
    main()
