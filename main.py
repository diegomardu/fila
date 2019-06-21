from Pessoa import *
from FilaPrioridade import *
p = Pessoa()
fila = FilaPrioridade()
while True:
    print("1 - Cadastra Pessoa:\n2 - Chamar:")
    n = int(input())
    if n == 1:
        p.setNome(input("Informe Nome:"))
        p.setIdade(int(input("Informe Idade:")))
        fila.cadastra(p)
    elif n == 2:
        busca = fila.chama()
        if busca:
            print(busca.getNome())
        else:
            print(busca)
