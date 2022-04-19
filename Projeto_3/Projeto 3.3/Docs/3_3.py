class Cartao:
    def __init__(self, num, data):
        self.num = num
        self.data = data
        self.cartoes = {}


def res():
    d = {}
    linha = input()
    while linha != "FIM":
        acao, *elems = input().split()
        if acao == "ACRESCENTA":
            nome, n_credito, date = elems
            temp_act = Cartao(n_credito, date)
            if nome in d:
                if n_credito in temp_act.cartoes:
                    print("NOVO UTILIZADOR CRIADO")
                temp_act.cartoes[n_credito] = date
                print("")
            else:
                d[nome]


def main():
    # res()
    a = Cartao(12, 12)


if __name__ == '__main__':
    main()