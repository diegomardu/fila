class Fila:
    def __init__(self, size):
        self._lista = [None]*size #tamanho fixo
        self._max = size
        self._inicio = 0
        self._n = 0
        
    def insere(self, v):
        if(self._n < self._max):
            pos = (self._inicio + self._n)%self._max
            self._lista[pos] = v
            self._n += 1
        else:
            raise Exception("Fila sem espaço")
    
    def retira(self):
        if(self._n > 0):
            val = self._lista[self._inicio]
            self._inicio = (self._inicio+1)%self._max
            self._n -= 1
            return val
        else:
            raise Exception("Fila vazia")
    
    def is_empty(self):
        return self._n == 0
    
    def __len__(self):
        return self._n
    
    def primeiro(self):
        return self._lista[self._inicio]
