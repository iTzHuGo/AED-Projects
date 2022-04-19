import random
import string

NUM_ARTIGOS = 10000

files = ["teste_c1_25000.txt", "teste_c1_50000.txt", "teste_c1_75000.txt", "teste_c1_100000.txt", "teste_c1_125000.txt",
         "teste_c2_25000.txt", "teste_c2_50000.txt", "teste_c2_75000.txt", "teste_c2_100000.txt", "teste_c2_125000.txt"]

count = 1
for name in files:
    if name.split('_')[1] == 'c1':
        f = open(name, "w")
        NUM_ACESSOS = int(name.split('_')[2].split('.')[0]) - NUM_ARTIGOS
        listanomes = []
        # ---------- ARTIGOS ALEATORIOS ---------------
        hashcharacters = string.ascii_lowercase + string.digits

        for i in range(NUM_ARTIGOS):
            linha = 'ARTIGO '
            nome = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
            listanomes.append(nome)
            nome += ' '
            hashvalue = ''.join(random.choice(hashcharacters) for _ in range(6))
            hashvalue += ' '
            value = str(random.randint(1, 1000))
            linha += nome
            linha += hashvalue
            linha += value
            linha += '\n'
            f.write(linha)

        # ---------- ACESSOS A CERTOS NOMES ------------

        nomes_consultados = []
        for _ in range(int(0.05 * NUM_ARTIGOS)):
            nome_random = random.choice(listanomes)
            nomes_consultados.append(nome_random)
            listanomes.remove(nome_random)

        percentage_to_number = 0.90 * NUM_ACESSOS
        print(nomes_consultados)

        for i in range(NUM_ACESSOS):
            if i >= percentage_to_number:
                nome = random.choice(listanomes)
            else:
                nome = random.choice(nomes_consultados)
            linha = 'CONSULTA '
            linha += nome
            linha += '\n'
            f.write(linha)

        # --------------------------------------------

        f.write('FIM')

        f.close()

    elif name.split('_')[1] == 'c2':
        f = open(name, "w")
        NUM_ACESSOS = int(name.split('_')[2].split('.')[0]) - NUM_ARTIGOS
        listanomes = []
        # ---------- ARTIGOS ALEATORIOS ---------------
        hashcharacters = string.ascii_lowercase + string.digits

        for i in range(NUM_ARTIGOS):
            linha = 'ARTIGO '
            nome = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
            listanomes.append(nome)
            nome += ' '
            hashvalue = ''.join(random.choice(hashcharacters) for _ in range(6))
            hashvalue += ' '
            value = str(random.randint(1, 1000))
            linha += nome
            linha += hashvalue
            linha += value
            linha += '\n'
            f.write(linha)
        # ---------- ACESSOS A NOMES ALEATORIOS --------
        for i in range(NUM_ACESSOS):
            nome = random.choice(listanomes)
            linha = 'CONSULTA '
            linha += nome
            linha += '\n'
            f.write(linha)
        f.write('FIM')

        f.close()
