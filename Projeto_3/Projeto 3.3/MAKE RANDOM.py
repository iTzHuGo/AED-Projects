import random
import string

NUM_TOTAL = 25000
NUM_REGISTOS = int(0.9 * NUM_TOTAL)
NUM_ACESSOS = int(0.1 * NUM_TOTAL)

f = open("testes252.txt", "w")

# ---------- REGISTOS ALEATORIOS ---------------

numcccharacters = string.ascii_lowercase + string.digits
listanomes = []

for i in range(NUM_REGISTOS):
    linha = 'ACRESCENTA '
    nome = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    listanomes.append(nome)
    nome += ' '
    numcc = ''.join(random.choice(numcccharacters) for _ in range(16))
    numcc += ' '
    validade = ''.join(random.choice(string.digits) for _ in range(4))
    linha += nome
    linha += numcc
    linha += validade
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