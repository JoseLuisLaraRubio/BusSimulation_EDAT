from Nodo import Nodo

class NodoDoble(Nodo):
    def __init__(self, dato,  anterior=None, siguiente=None):
        super().__init__(dato, siguiente)
        self._anterior = anterior
    
    @property
    def anterior(self):
        return self._anterior 
    
    @anterior.setter
    def anterior(self,anterior):
        self._anterior = anterior