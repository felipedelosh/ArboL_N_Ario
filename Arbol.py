"""
04 21 2019


para ingresar un padre .insertarDato(IDpadre)
para ingresar un hijo .insertarDato(hijo, IDpadre)

OJo: en caso de no ingresarse el padre se guardara en la raiz


"""

"""Este modulo se importa para calcular la altura del arbol"""


class Nodo:
    def __init__(self, ID):
        self.padre = ID
        self.hijos = []

class ArbolN:
    def __init__(self):
        self.raiz = None
        """Esta variable controla la profundidad del arbol"""
        self.profundidad = 0

    def insertarDato(self, dato, padre=0, nodo=0):
        """Si la raiz esta vacia procedo a crear"""
        if self.raiz == None:
            self.raiz = Nodo(dato)
        else:
            """Sera que estoy parado en el padre?"""
            if self.raiz.padre == padre:
                self.raiz.hijos.append(Nodo(dato))
            else:
                """Procedo a buscar al padre"""
                temporal = self.buscarNodo(padre, self.raiz.hijos)

                if temporal == None:
                    print('El ID :' + str(padre) + " No existe")
                else:
                    temporal.hijos.append(Nodo(dato))

    """
    Ojo: este metodo es el auxiliar de insertar
    
    IDnodo: es la key que caracteriza al padre
    nodos es un vector de hijos
    """
    def buscarNodo(self, IDnodo, nodos, contador=0):
        """Controlo que no se desborde el arreglo"""
        if contador >= len(nodos):
            return None

        """Sera que lo encontre?"""
        if nodos[contador].padre == IDnodo:
            return nodos[contador]

        """Busco entre los hijos"""
        temp = self.buscarNodo(IDnodo, nodos[contador].hijos)
        if temp != None:
            return temp

        """Busco entre los hermanos"""
        temp = self.buscarNodo(IDnodo, nodos, contador+1)
        if temp != None:
            return temp

        """Entonces no existe"""
        return None

    """Este metodo imprime todos los nodos
    Padre, luego los hijos
    """
    def imprimirArbol(self, nodo):
        if nodo != None:
            print(nodo.padre)
            for i in nodo.hijos:
                self.imprimirArbol(i)

    """Este metodo imprime los hijos de un padre"""
    def imprimirHijos(self, IDpadre):
        if self.raiz.padre == IDpadre:
            for i in self.raiz.hijos:
                print(i.padre)
        else:
            temporal = self.buscarNodo(IDpadre, self.raiz.hijos)

            if temporal == None:
                print('Ese nodo no existe: ', IDpadre)
            else:
                for i in temporal.hijos:
                    print(i.padre)

    """Este metodo me retorna en un vector todos los ID de los nodos [ID, ID, ID, ID]"""
    def vectorizar(self, nodo, vector=[]):
        if nodo != None:
            vector.append(nodo.padre)

            for i in nodo.hijos:
                self.vectorizar(i)

        return vector

    """Este medoto retorna cuantos hijos tiene un padre"""
    def cuantosHijosTieneX(self, IDpadre):
        if self.raiz.padre == IDpadre:
            return len(self.raiz.hijos)
        else:
            temporal = self.buscarNodo(IDpadre, self.raiz.hijos)

            if temporal == None:
                return 0
            else:
                return len(temporal.hijos)

    """Este metodo me dice si un nodo tiene hijos"""
    def nodoXtieneHijos(self, IDpadre):
        if self.raiz.padre == IDpadre:
            return len(self.raiz.hijos) > 0
        else:
            temporal = self.buscarNodo(IDpadre, self.raiz.hijos)

            if temporal == None:
                return False
            else:
                return len(temporal.hijos) > 0


    """Este metodo retorna cual es la cantidad maxima de hijos en todo el arbol"""
    def cantidadMaximaDeHijos(self):
        temporal = self.vectorizar(self.raiz)

        nro_hijos = 0

        for i in temporal:
            aux = self.cuantosHijosTieneX(i)

            if aux > nro_hijos:
                nro_hijos = aux

        return nro_hijos

    def actualizarProfundidad(self, nodos, contador=0, auxiliar=0):
        """Si estoy en una hoja actualizo la profundidad"""
        if contador>=len(nodos):
            if auxiliar > self.profundidad:
                self.profundidad = auxiliar
            return None

        """Me meto por los hijos"""
        self.actualizarProfundidad(nodos[contador].hijos,0, auxiliar+1)
        """Me meto por los hermanlos"""
        self.actualizarProfundidad(nodos, contador+1, auxiliar)




















# dato, padre, raiz
a =  ArbolN()
a.insertarDato(0)
a.insertarDato(1)
a.insertarDato(2)
a.insertarDato(3, 0, a.raiz)
a.insertarDato(4, 0, a.raiz)
a.insertarDato(5, 0, a.raiz)


a.insertarDato(9, 1, a.raiz)
a.insertarDato(10, 9, a.raiz)
a.insertarDato("AFH", 10, a.raiz)


a.insertarDato(11, 3, a.raiz)
a.insertarDato(12, 11, a.raiz)


a.insertarDato(99, 5, a.raiz)

a.insertarDato("A", 99, a.raiz)
a.insertarDato("B", 99, a.raiz)
a.insertarDato("C", 99, a.raiz)
a.insertarDato("D", 99, a.raiz)
a.insertarDato("E", 99, a.raiz)

a.insertarDato("U", "C", a.raiz)
a.insertarDato("F", "U", a.raiz)
a.insertarDato("O", "F", a.raiz)



print('Estos son todos los nodos: ', a.vectorizar(a.raiz))
print('AFE tiene hijos? ', a.nodoXtieneHijos("AFE"))
print('El numero de hijos de 3 es ', a.cuantosHijosTieneX(3))
print('El mayor numero de hijos es: ', a.cantidadMaximaDeHijos())
a.actualizarProfundidad(a.raiz.hijos)
print('La profundidad es: '+str(a.profundidad))
print('Los hijos de c, u, f ')
a.imprimirHijos("C")
a.imprimirHijos("U")
a.imprimirHijos("F")

