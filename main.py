from FilaPrioridade import *
from Pessoa import*
fila=FilaPrioridade()
while True:
    print('1 - Cadastra Pessoa:\n2 - Chamar:')
    n = int(input())
    if n == 1:
        nome = (input("Informe Nome:"))
        idade = (int(input('Informe a idade:')))
        p = Pessoa(nome,idade)
        fila.cadastra(p)
    elif n == 2:
        busca = fila.chama()
        print(busca.getNome())


