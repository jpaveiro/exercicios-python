import os

while opcao != 0:
    os.system("cls")

    print("""
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
    """)

    def twoValues():
        n1 = float(input("Digite o 1 numero: "))
        n2 = float(input("Digite o 2 numero: "))
        if n1 > n2:
            print(f"O numero maior e {n1}")
        elif n1<n2:
            print(f"O numero maior e {n2}")
        else:
            print("Nao tem maior")

    def birthyearVote():
        birthyear = int(input("Qual seu ano de nascimento? "))
        if birthyear > 2006:
            print("Nao pode votar")
        else:
            print("Pode votar")

    def passwordVerify():
        password = int(input("Digite a senha: "))
        if password == 1234:
            print("Acesso permitido")
        else:
            print("Acesso negado")

    def appleValue():
        appleBuyed = float(input("Quantas maças foram compradas? "))

        if appleBuyed < 12:
            vt = appleBuyed * 0.3
            print(f"O valor total da compra e: {vt}")
        else:
            vt = appleBuyed * 0.25
            print(f"O valor total da compra e: {vt}")

    def threeValuesCrescent():
        value1 = int(input("Digite um valor:"))
        value2 = int(input("Digite outro valor:"))
        value3 = int(input("Digite mais um valor:"))
        ordCres = [value1,value2,value3] 
        ordCres.sort()
        print(f"A ordem crescente e {ordCres}")

    def idealWeight():
        height = float(input("Qual sua altura:"))
        sex = int(input("Você é - 1:feminino 2:masculino? "))
    
        if sex == 1:
            weightIdeal = (62.1 * height) - 44.7
            print(f"O seu peso ideal é {weightIdeal:.2f}")
        elif sex == 2:
            weightIdeal = (72.7 * height) - 58
            print(f"O seu peso ideal é {weightIdeal:.2f}")
        else:
            print("Eu simplesmente nao existo, ha apenas uma ideia de patrick bateman")

    def regularPolygon():
        numberSide = int(input("Digite o numero de lados:"))
        sidecm = float(input("Quantos centimetros tem um lado do poligono? "))

        if numberSide < 3:
            print("Nao e um poligono")
        elif numberSide == 3:
            area = sidecm*sidecm*1.7/4.0
            print(f"TRIANGULO {area:.2f}")
        elif numberSide == 4:
            area = sidecm*sidecm
            print(f"QUADRADO {area:.2f}")
        elif numberSide == 5:
            print(f"PENTAGONO")
        else:
            print("Poligono nao identificado")

    def threeValuesBiggest():
        value1 = int(input("Digite um valor:"))
        value2 = int(input("Digite outro valor:"))
        value3 = int(input("Digite mais um valor:"))

        if value1 > value2 and value1 > value3:
            biggestValue = value1
        elif value2 > value1 and value2 > value3:
            biggestValue = value2
        else:
            biggestValue = value3
        print(f"O maior valor é {biggestValue}")

    def trianguleDefinition():
        sidecm1 = float(input("Quantos centimetros tem um lado do triangulo? "))
        sidecm2 = float(input("Quantos centimetros tem o outro lado do triangulo? "))
        sidecm3 = float(input("Quantos centimetros tem o ultimo lado do triangulo? "))

        if sidecm1 == sidecm2 and sidecm1 == sidecm3:
            print("Triangulo equilatero possui 3 lados iguais")
        elif sidecm1 == sidecm2 or sidecm1 == sidecm3:
            print("Triangulo Isosceles possui 2 lados iguais")
        else:
            print("Triangulo escaleno possui 3 lados diferentes")

    def trianguleAngule():
        angule1 = float(input("Qual o 1 angulo? "))
        angule2 = float(input("Qual o 2 angulo? "))
        angule3 = float(input("Qual o 3 angulo? "))

        if angule1 == 90 or angule2 == 90 or angule3 == 90:
            print("Triangulo Retangulo")
        elif angule1 >= 90 or angule2 >= 90 or angule3 >= 90:
            print("Triangulo Obtusangulo")
        else:
            print("Triangulo Acutangulo")

    opcao = int(input("Digite um exercicio:"))

    match opcao:
        case 0:
            print("Finalizando execução")
            break
        case 1:
            twoValues()
        case 2:
            birthyearVote()
        case 3:
            passwordVerify()
        case 4:
            appleValue()
        case 5:
            threeValuesCrescent()
        case 6:
            idealWeight()
        case 7:
            regularPolygon()
        case 8:
            regularPolygon()
        case 9:
            threeValuesBiggest()
        case 10:
            trianguleDefinition()
        case 11:
            trianguleAngule()
        case _:
            print("Digite uma opcao existente")

    os.system("pause")
