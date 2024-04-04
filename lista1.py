import os
from funcoes_lista1 import Funcao

continuar = True

while (continuar):
    os.system("cls")
    opcao = int(input("Digite o número do exercício que deseja executar (1 até 11)\n=> "))

    match(opcao):
        case 0:
            print("Saindo do programa. Obrigado por testar!")
            continuar = False
        case 1:
            n1 = int(input("Digite um número:\n=> "))
            n2 = int(input("Digite outro número:\n=> "))
            Funcao.comparacao(n1, n2)
        case 2:
            anoNascimento = int(input("Digite um ano:\n=> "))
            Funcao.podeVotar(anoNascimento)
        case 3:
            senha = str(input("Digite a senha:"))
            Funcao.senhaCorreta(senha)
        case 4:
            nmrMacas = int(input("Digite a quantidade de maçãs que deseja comprar:\n=> "))
            Funcao.comprarMaca(nmrMacas)
        case 5:
            n1 = int(input("Digite o primeiro número:\n=> "))
            n2 = int(input("Digite o segundo número:\n=> "))
            n3 = int(input("Digite o terceiro número:\n=> "))
            Funcao.ordemCrescente(n1, n2, n3)
        case 6:
            altura = float(input("Digite sua altura:\n=> "))
            sexo = int(input("Digite 1 para Feminino ou 2 para Masculino:\n=> "))
            Funcao.pesoIdeal(altura, sexo)
        case 7:
            numeroLados = int(input("Digite o número de lados:\n=> "))
            cmLados = float(input("Digite quantos cm tem cada lado:\n=> "))
            Funcao.poligono(numeroLados, cmLados)
        case 8:
            valor1 = int(input("Digite o primeiro valor:\n=> "))
            valor2 = int(input("Digite o segundo valor:\n=> "))
            valor3 = int(input("Digite o terceiro valor:\n=> "))
            Funcao.maiorDosTres(valor1, valor2, valor3)
        case 9:
            angulo1 = float(input("Digite o primeiro ângulo:\n=> "))
            angulo2 = float(input("Digite o segundo ângulo:\n=> "))
            angulo3 = float(input("Digite o terceiro ângulo:\n=> "))
            Funcao.definicaoTriangulo(angulo1, angulo2, angulo3)
        case 10:
            angulo1 = float(input("Digite o primeiro ângulo:\n=> "))
            angulo2 = float(input("Digite o segundo ângulo:\n=> "))
            angulo3 = float(input("Digite o terceiro ângulo:\n=> "))
            Funcao.anguloTriangulo(angulo1, angulo2, angulo3)
        case 11:
            numero = int(input("Digite o ângulo que deseja obter o fatorial:\n=> "))
            Funcao.fatorial(numero)
        case _:
            print("Opção inválida.")

    os.system("pause")
