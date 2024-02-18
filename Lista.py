class Lista():
    def __init__(self,nombre='Lista',inicio=None,ultimo=None):
        self._inicio = inicio
        self._ultimo = ultimo
        self._nombre = nombre

    def is_empty(self):
     return self._inicio == None
    
    def __str__(self):
        lista = ''
        actual = self._inicio
        while actual!=None:
            lista += str(actual.dato) + "->"
            actual = actual.siguiente  
        return lista[:-2]
    
    def inserta_inicio(self, dato):
        pass
    
    def inserta_final(self, dato):
        pass
    
    def elimina_inicio(self):
        pass
    
    def elimina_final(self):
        pass
    
    @property
    def inicio(self):
        return self._inicio

    @inicio.setter
    def inicio(self, inicio):
        self._inicio = inicio
    
    @property
    def ultimo(self):
        return self._ultimo

    @ultimo.setter
    def ultimo(self, ultimo):
        self._ultimo = ultimo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre