from os import system
clear = system("cls")
continuar = True

# 1 ao 5
v = [45, -89, 32, -12, 33]
def primeiro_elemento(vetor: list) -> int:
    return vetor[0]

def exibe_negativos(vetor: list) -> None:
    for i in vetor:
        if i < 0:
            print(i)

def soma_elementos(vetor: list) -> int:
    soma = 0
    for i in vetor:
        soma+= i
    return soma

def media_elementos(vetor: list) -> float:
    soma = 0
    n_itens = 0
    for i in vetor:
        soma+= i
        n_itens += 1
    return soma / n_itens

def elementos_impares(vetor: list) -> None:
    for i in vetor:
        if i % 2 == 1:
            print(i)

# 6 ao 9
def exibe_extremos(vetor: list) -> None:
    print(vetor.pop(0), vetor.pop())

def exibe_indice_impar(vetor: list) -> None:
    count = 0
    for i in vetor:
        if (count % 2 == 1):
            print(vetor[count])
        count += 1

def busca(vetor: list, numero: int) -> bool:
    for i in vetor:
        if i == numero:
            print(i)
            return True
    
    return False

def ordena(v: list) -> None:
    v.sort()
    print(str(v).replace("[", "").replace("]", ""))

# 10 ao 13
v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

def copia_vetor(v1: list, v2: list) -> None:
    v2 = v1.copy()

    print("v1 =", str(v1).replace("[", "").replace("]", ""))
    print("v2 =", str(v2).replace("[", "").replace("]", ""))

def inverte_vetor(v1: list, v2: list) -> None:
    v2 = v1.copy()
    v2.reverse()
    print("v1 =", str(v1).replace("[", "").replace("]", ""))
    print("v2 =", str(v2).replace("[", "").replace("]", ""))

def ordena_vetor_crescente(vetor: list) -> None:
    vetor.sort()
    print("vetor =", str(vetor).replace("[", "").replace("]", ""))

def ordena_vetor_descrescente(vetor: list) -> None:
    vetor.sort()
    vetor.reverse()
    print("vetor =", str(vetor).replace("[", "").replace("]", ""))

# 14 ao 17
def ordena_vetor(vetor: list, tipo: str) -> None:
    match(tipo.lower()):
        case "c":
            ordena_vetor_crescente(vetor)
        case "d":
            ordena_vetor_descrescente(vetor)
        case _:
            print("Tipo de ordem inválida.")

def separa_pares_impares(vetor: list) -> None:
    esquerda = []
    direita = [] 

    for i in vetor:
        if i % 2 == 0:
            esquerda.append(i) 
        else:
            direita.append(i) 

    print(str(esquerda + direita).replace("[", "").replace("]", ""))

def conta_acima_media(vetor: list) -> int:
    media = 0
    contador = 0

    for i in vetor:
        media += i

    media = media / len(vetor)

    for i in vetor:
        if i > media:
            contador += 1
    return contador

def maior_elemento(vetor: list):
    maior_elemento = -999999999
    for i in vetor:
        if i > maior_elemento:
            maior_elemento = i
    return maior_elemento
