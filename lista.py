from os import system
from exercicios_python.funcao import Funcao

opcao = None

while opcao != 0:
    print('''
    0 - para sair
    exercicio 1 - 2 valores
    exercicio 2 - Ano de nascimento
    exercicio 3 - Validade senha
    exercicio 4 - Valor total maças
    exercicio 5 - 3 valores inteiros
    exercicio 6 - Peso ideal
    exercicio 7 e 8 - Poligno regular
    exercicio 9 - 3 valores inteiros, exibir maior
    exercicio 10 - Triangulo Equilatero, Isosceles ou Escaleno
    exercicio 11 - Triangulo Acutangulo, Retangulo, Obtusangulo
''')
    opcao = int(input("Selecione um exercício: \n=> "))