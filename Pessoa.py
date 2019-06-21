class Pessoa:
    def __init__(self,nome="",idade=0):
        self._nome = nome
        self._idade = idade

    def getNome(self):
        return self._nome
    def setNome(self,nome):
        self._nome = nome

    def getIdade(self):
        return self._idade
    def setIdade(self,idade):
        self._idade = idade
