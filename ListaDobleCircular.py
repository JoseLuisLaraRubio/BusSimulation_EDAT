from NodoDoble import NodoDoble
from Lista import Lista

class ListaDobleC(Lista):
    def inserta_inicio(self, dato) -> None:
        """Overrides Lista.inserta_inicio()"""
        if self.is_empty():
            self.inicio = NodoDoble(dato)
            self.ultimo = self.inicio
            self.inicio.siguiente = self.inicio
            self.inicio.anterior = self.ultimo
        else:
            nuevo = NodoDoble(dato,anterior=self.ultimo,
                            siguiente = self.inicio)
            self.ultimo.siguiente = nuevo                            
            self.inicio.anterior = nuevo
            self.inicio = nuevo
    
    def inserta_final(self, dato) -> None:
        if self.is_empty():
            self.ultimo = NodoDoble(dato)
            self.inicio = self.ultimo
            self.inicio.siguiente = self.inicio
            self.inicio.anterior = self.ultimo
        else:
            nuevo = NodoDoble(dato, anterior = self.ultimo, siguiente = self.inicio)
            self.ultimo.siguiente = nuevo
            self.inicio.anterior = nuevo
            self.ultimo = nuevo

    def elimina_inicio(self):
        if self.is_empty():
            print('La lista está vacía')
        else:
            eliminado = self.inicio.dato
            self.inicio = self.inicio.siguiente
            self.inicio.anterior = self.ultimo
        return eliminado
    
    def elimina_final(self):
        if self.is_empty():
            print('La lista está vacía')
        else:
            eliminado = self.ultimo.dato
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = self.inicio
        return eliminado

    def inserta_antes(self, dato_insertar, dato_encontrar) -> None:
        if self.is_empty(): self.inserta_inicio(dato_insertar)
        else:
            actual = self.buscar_dato(dato_encontrar)
            if actual == None: pass #¿Que hacer?
            else:
                if actual == self.inicio: self.inserta_inicio(dato_insertar)
                else:
                    nuevo = NodoDoble(dato_insertar,actual.anterior,actual)
                    actual.anterior.siguiente = nuevo
                    actual.anterior = nuevo

    def inserta_despues(self, dato_insertar, dato_encontrar) -> None:
        if self.is_empty(): self.inserta_inicio(dato_insertar)
        else:
            actual = self.buscar_dato(dato_encontrar)
            if actual == None: pass #¿Que hacer?
            else:
                if actual == self.ultimo: self.inserta_final(dato_insertar)
                else:
                    nuevo = NodoDoble(dato_insertar,actual,actual.siguiente)
                    actual.siguiente.anterior = nuevo
                    actual.siguiente = nuevo

    def imprime_al_reves(self) -> str:
        if self.is_empty(): print('La lista está vacía')
        else:
            actual = self.ultimo
            lista = ''
            while True:
                lista += str(actual.dato) + "->"
                actual = actual.anterior
                if actual==self.ultimo: break
            return lista[:-2]
        
    def imprime_al_derecho(self) -> str:
        if self.is_empty(): print('La lista está vacía')
        else:
            actual = self.inicio
            lista = ''
            while True:
                lista += str(actual.dato) + "->"
                actual = actual.siguiente
                if actual==self.inicio: break
            return lista[:-2]

    def buscar_dato(self, dato) -> NodoDoble:
        #Determinar si el dato se encuentra más cerca del inicio o final
        actual = self.inicio
        while actual.siguiente !=  self.inicio:
            if actual.dato == dato: return actual
            actual = actual.siguiente
        return None

    def len(self):
        actual = self.inicio
        size = 1

        while actual.siguiente != self.inicio:
            actual = actual.siguiente
            size += 1
        
        return size