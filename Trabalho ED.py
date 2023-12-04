#Salvando o cadastro
nomedoarquivo = 'TrabalhoED.bin'
cadastroclientes = dict()

#Importando dados
import os
import pickle
if os.path.isfile(nomedoarquivo):
    with open(nomedoarquivo, 'rb') as arquivo:
        cadastroclientes = pickle.load(arquivo)
        
#Apresentação do programa
print(f'\033[1;35m-------------------------------------------------------------------------------------\033[m')
print(f'\033[1;35mOlá! Seja bem vindo(a) a Fashion Beauty!\033[m')
print('')
print('\033[1;35mORIENTAÇÔES\033[m')
print(f'\033[1;35mAntes de começarmos, cadastre-se ou faça o log in para continuarmos sua compra!\033[m')
print(f'\033[1;35mResponda as perguntas seguintes com Sim ou Não ou de acordo com as orientações dadas.\033[m')
print('')
print(f'\033[1;35m-------------------------------------------------------------------------------------\033[m')

#Implementando um cadastro
def cadastro_clientes(cadastroclientes):
    client = input(f'\033[1;35mVocê já possui cadastrado em nossa loja? \033[4;31m(Sim/Não)\033[m: \033[m')
    print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
    if client.upper() == 'NAO' or client.upper() == 'NÃO':
        nome = input(f'\033[1;35mQual é o seu nome completo?: \033[m')
        print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
        idade = input(f'\033[1;35mVoce tem quantos anos?: \033[m')
        print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
        sexo = input(f'\033[1;35;mVocê é homem ou mulher? \033[4;31m(H/M)\033[m: ')
        print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
        telefone = input(f'\033[1;35mQual seu telefone? \033[4;31m(DD-XXXXXXXXX)\033[m: \033[m')
        print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
        cadastroclientes[telefone] = nome, idade, sexo
        print(f'\033[1;35m{nome} seu cadastro foi feito com sucesso!\033[m')
        client_name = cadastroclientes[telefone][0]
    else:
        eh_cliente()
    return cadastroclientes
client_name = ''
def eh_cliente():
    global client_name
    telefone = input(f'\033[1;35mQual o seu numero de telefone? \033[4;31m(DD-XXXXXXXXX)\033[m: \033[m')
    print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
    if telefone not in cadastroclientes:
        print(f'\033[1;35mVocê ainda não possui cadastro em nossa loja!\033[m')
        cadastro_clientes(cadastroclientes)
    else:
        if cadastroclientes[telefone][2].upper() == 'M':
            print(f'\033[1;35mOlá {cadastroclientes[telefone][0]}, seja bem vinda a Fashion Beauty!\033[m')
            print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
            client_name = cadastroclientes[telefone][0]
            return client_name
        else:
            print(f'\033[1;35mOlá {cadastroclientes[telefone][0]}, seja bem vindo a Fashion Beauty!\033[m')
            print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
            client_name = cadastroclientes[telefone][0]
            return client_name


cadastro_clientes(cadastroclientes)        
#Salva Cadastro
with open(nomedoarquivo, 'wb') as arquivo:
    pickle.dump(cadastroclientes, arquivo)

#Classes
class Noh:
    def __init__(self, key, name, quant):
        self.key = key
        self.name = name
        self.quant = quant
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree:
    def height(self, noh):
        if not noh:
            return 0
        return noh.height

    def balance(self, noh):
        if not noh:
            return 0
        return self.height(noh.left) - self.height(noh.right)
#Rotações
    def left_rotation(self, aux_1):
        aux_2 = aux_1.right
        T2 = aux_2.left

        aux_2.left = aux_1
        aux_1.right = T2

        aux_1.height = 1 + max(self.height(aux_1.left), self.height(aux_1.right))
        aux_2.height = 1 + max(self.height(aux_2.left), self.height(aux_2.right))

        return aux_2

    def right_rotation(self, aux_2):
        aux_3 = aux_2.left
        T2 = aux_3.right

        aux_3.right = aux_2
        aux_2.left = T2

        aux_2.height = 1 + max(self.height(aux_2.left), self.height(aux_2.right))
        aux_3.height = 1 + max(self.height(aux_3.left), self.height(aux_3.right))

        return aux_3
#Inserção
    def insert(self, root, key, name, quant):
        if not root:
            return Noh(key, name, quant)
        elif key < root.key:
            root.left = self.insert(root.left, key, name, quant)
        else:
            root.right = self.insert(root.right, key, name, quant)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotation(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotation(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)

        return root
#Valor Mínimo
    def noh_min_value(self, noh):
        current = noh
        while current.left:
            current = current.left
        return current
#Remoção
    def remove(self, root, key, name, quant):
        if not root:
            return root

        if key < root.key:
            root.left = self.remove(root.left, key, name, quant)
        elif key > root.key:
            root.right = self.remove(root.right, key, name, quant)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.noh_min_value(root.right)
            root.name = temp.name
            root.key = temp.key
            root.quant = temp.quant
            root.right = self.remove(root.right, temp.key, temp.name, temp.quant)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotation(root)

        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotation(root)

        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)

        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)

        return root
#Em Ordem
    def in_order(self, root):
        res = []
        if root:
            price = len(root.name)*0.25*int(root.quant)
            res = self.in_order(root.left)
            res.append([root.quant, root.name,'R$', price])
            res = res + self.in_order(root.right)
        return res

# Tabela
print('\033[1;35mAqui estão os produtos Fashion Beauty\033[m')
print(f"\033[1;35mCada produto está associado a um código \033[4;31m'XX'\033[m \033[1;35mque o acompanha\033[m")
print(f'\033[1;35m=============================================================================================================\033[m')
print(f"|{'10 Base R$ 1,00':^26}|{'15 Rímel R$ 1,25':^26}|{'20 Sombra R$ 1,50':^26}|{'25 Pó-Compacto R$ 2,75':^26}|")
print(f'\033[1;35m=============================================================================================================\033[m')
print(f"|{'30 Delineador R$ 2,25':^26}|{'35 Batom R$ 1,25':^26}|{'40 Iluminador R$ 2,25':^26}|{'45 Primer-Facial R$ 2,24':^26}|")
print(f'\033[1;35m=============================================================================================================\033[m')
print(f"|{'50 Corretivo R$ 2,25':^26}|{'55 Gloss-Labial R$ 3,00':^26}|{'60 Blush R$ 1,25':^26}|{'65 Fixador R$ 1,50':^26}|")
print(f'\033[1;35m=============================================================================================================\033[m')
print(f"|{'70 Demaquilante R$ 3,00':^26}|{'75 Máscara-Facial R$ 3,50':^26}|{'80 Bronzeador R$ 2,25':^26}|{'85 Água-Micelar R$ 3,00':^26}|")
print(f'\033[1;35m=============================================================================================================\033[m')
print(f"|{'90 Spray-Fixador R$ 3,25':^26}|{'95 Lápis-de-Olho R$ 3,25':^26}|{'90 Cílios-Postiços R$ 3,75':^26}|{'95 Esponja R$ 1,75':^26}|")
print(f'\033[1;35m=============================================================================================================\033[m')
print(f"|{'100 Pínceis R$ 1,75':^26}|{'105 Lenços-Humidos R$ 3,55':^26}|{'110 Esfoliante R$ 2,50':^26}|{'115 Pó-Translúcido R$ 3,25':^26}|")
print(f'\033[1;35m=============================================================================================================\033[m')

# Perguntas e Respostas:
trolley = AVL_Tree()
root = None
total = 0

def add_trolley(Q1):
    global root
    global total
    if Q1.upper() != 'NAO' and Q1.upper() != 'NÃO':
        print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
        Q2 = input(f'\033[1;35mQual produto você gostaria de adicionar? \033[4;31mXX Produto Quantidade\033[m: ').split()
        print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
        total += int(Q2[2])*0.25*len(Q2[1])
        print(f'\033[1;35mO produto {Q2[1]} foi adicionado ao seu carrinho!\033[m')
        print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
        root = trolley.insert(root, int(Q2[0]), Q2[1], Q2[2])
        add_trolley(Q1 = input('\033[1;35mVocê gostaria de adicionar algum item ao carrinho? \033[4;31m(Sim/Não)\033[m: '))
    return total
add_trolley(Q1 = input('\033[1;35mVocê gostaria de adicionar algum item ao carrinho? \033[4;31m(Sim/Não)\033[m: '))

print("\033[1;35mEste é seu carrinho!\033[m")
print("\033[1;35m[Quantidade, Produto, Preço]\033[m")
print(trolley.in_order(root))
print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')

def remove_trolley(Q3):
    global root
    global total 
    if Q3.upper() == 'SIM':
        print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
        Q4 = input('\033[1;35mQual produto você gostaria de remover? \033[4;31mXX-Produto-Quantidade\033[m: ').split()
        print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
        total -= int(Q4[2])*0.25*len(Q4[1])
        print(f'\033[1;35mO produto {Q4[1]} foi retirado do seu carrinho!\033[m')
        print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
        root = trolley.remove(root, int(Q4[0]), Q4[1], Q4[2])
        remove_trolley(Q3 = input('\033[1;35mVocê gostaria de retirar algum item do carrinho? \033[4;31m(Sim/Não)\033[m: '))
    return total 

Q5 = input('\033[1;35mVocê gostaria de encerrar sua compra? \033[4;31m(Sim/Não)\033[m: ')
if Q5.upper() == 'SIM':
    print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
    remove_trolley(Q3 = input('\033[1;35mVocê gostaria de retirar algum item do carrinho? \033[4;31m(Sim/Não)\033[m: '))
else:
    add_trolley(Q1 = input('\033[1;35mVocê gostaria de adicionar algum item ao carrinho? \033[4;31m(Sim/Não)\033[m: '))
def final():
    print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
    print("\033[1;35mEste é seu carrinho\033[m")
    print("\033[1;35m[Quantidade, Produto, Preço]\033[m")
    print(trolley.in_order(root))
    print(f'\033[1;35m------------------------------------------------------------------------------------\033[m')
    print(f'\033[1;35mO total da sua compra foi de R$ {total}\033[m')
    Q9 = input('\033[1;35mVocê gostaria de pagar no crédito ou no débito? \033[m')
    print('\033[1;35mPagamento aceito.\033[m')
    print(f'\033[1;35m{client_name} volte sempre para aproveitar as ofertas do Fashion Beauty!\033[m')
    print('\033[1;35m:):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):)\033[m')
final()