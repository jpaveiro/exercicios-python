class Funcao:
    def __init__():
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
        
Funcao.ordemCrescente(8, 5, 7)