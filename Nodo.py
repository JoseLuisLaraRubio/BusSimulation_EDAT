class Nodo():
    def __init__(self,dato,siguiente=None):
        self._dato = dato
        self._siguiente = siguiente
    
    @property
    def dato(self):
        return self._dato
    
    @dato.setter
    def dato(self, dato):
        self._dato = dato
    
    @property
    def siguiente(self):
        return self._siguiente
    
    @siguiente.setter
    def siguiente(self, siguiente):
        self._siguiente = siguiente