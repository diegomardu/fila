from Fila import *
class FilaPrioridade:
    def __init__(self):
        self._filan = Fila(100)
        self._filaP = Fila(100)

    def cadastra(self,pessoa):
        if pessoa.getIdade() >= 65:
            self._filaP.insere(pessoa)
        else:
            self._filan.insere(pessoa)

    def chama(self):
        if not (self._filaP.is_empty()):
            return self._filaP.retira()
        elif not(self._filan.is_empty()):
            return self._filan.retira()
        return None




