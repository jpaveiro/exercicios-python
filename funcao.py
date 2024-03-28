class Funcao:
    def __init__(self):
        pass

    def comparacao(a: int, b: int):
        if a > b:
            print("A é maior que B")
        else:
            print("B é maior que A")

    def podeVotar(anoNascimento: int):
        if ((2024 - anoNascimento) >= 18):
            print("Pode votar!")
        else:
            print("Não pode votar!")

    def senhaCorreta(senha: str):
        if senha == "1234":
            print("ACESSO PERMITIDO")
        else:
            print("ACESSO NEGADO")

    def comprarMaca(quantidade: int):
        if quantidade >= 12:
            valorMaca = 0.25
            print("Quantidade de maças: {0}\nTOTAL:\tR$ {1}".format(quantidade, (valorMaca * quantidade)))
        else:
            valorMaca = 0.30
            print("Quantidade de maças: {0}\nTOTAL:\tR$ {1}".format(quantidade, (valorMaca * quantidade)))

    def ordemCrescente(n1: int, n2: int, n3: int):
        ordem = [n1, n2, n3]
        ordem.sort()
        print("Ordem crescente:", ordem)

    def pesoIdeal(altura: float, sexo: int):
        if (sexo == 1): # Feminino
            pesoIdeal = (62.1 * altura) - 44.7
        elif (sexo == 2): # Masculino
            pesoIdeal = (72.7 * altura) - 58
        else:
            print("Sexo inválido.")
            return
        print("Seu peso ideal é:", pesoIdeal)

    def poligono(numeroLados: int, cmLados: float):
        if numeroLados < 3:
            print("Nao e um poligono")
        elif numeroLados == 3:
            area = cmLados*cmLados*1.7/4.0
            print(f"TRIANGULO {area:.2f}")
        elif numeroLados == 4:
            area = cmLados*cmLados
            print(f"QUADRADO {area:.2f}")
        elif numeroLados == 5:
            print(f"PENTAGONO")
        else:
            print("Poligono nao identificado")

    def maiorDosTres(valor1: int, valor2: int, valor3: int):
        if (valor1 > valor2 and valor1 > valor3):
            maiorValor = valor1
        elif (valor2 > valor1 and valor2 > valor3):
            maiorValor = valor2
        else:
            maiorValor = valor3

        return maiorValor
    
    def definicaoTriangulo(lado1cm: float, lado2cm: float, lado3cm: float):
        if lado1cm == lado2cm and lado1cm == lado3cm:
            print("Triangulo equilatero possui 3 lados iguais")
        elif lado1cm == lado2cm or lado1cm == lado3cm:
            print("Triangulo Isosceles possui 2 lados iguais")
        else:
            print("Triangulo escaleno possui 3 lados diferentes")

    def trianguleAngule(angulo1: float, angulo2: float, angulo3: float):
        if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
            print("Triangulo Retangulo")
        elif angulo1 >= 90 or angulo2 >= 90 or angulo3 >= 90:
            print("Triangulo Obtusangulo")
        else:
            print("Triangulo Acutangulo")

    def fatorial(nmr: int):
        fatorial = nmr
        nmr = nmr - 1
        for i in range(1, nmr):
            fatorial = fatorial * nmr
            nmr = nmr - 1
        print(f"O fatorial é {fatorial}")
