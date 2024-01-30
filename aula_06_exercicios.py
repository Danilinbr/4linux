# 1) Crie uma classe que represente um ônibus. O ônibus deverá conter os seguintes atributos:

# capacidade total
# capacidade atual
# placa
# modelo
# movimento

# Os comportamentos esperados para um Ônibus são:

# Embarcar
# Desembarcar
# Acelerar
# Frear

# Lembre-se que a capacidade total do ônibus é de 45 pessoas - não será possível admitir super-
# lotação. Além disso, quando o ônibus ficar vazio, não será permitido efetuar o desembarque
# de pessoas. Além disso, pessoas não podem embarcar ou desembarcar com o onibus em movimento.
class Onibus:
    def __init__(self, capacidade_total, placa, modelo):
        self.__capacidade_total = capacidade_total
        self.__capacidade_atual = 0
        self.__placa = placa
        self.__modelo = modelo
        self.__movimento = False
        print(f"Onibus preparado para serviço!\nplaca: {self.__placa}. Modelo: {self.__modelo}")

    def get_capacidade_atual(self):
        return self.__capacidade_atual

    def set_capacidade_atual(self, nova_capacidade):
        if nova_capacidade >= 0 and nova_capacidade <= self.__capacidade_total:
            self.__capacidade_atual = nova_capacidade
        else:
            print("Capacidade inválida.")

    def embarcar(self, quantidade):
        if not self.__movimento and (self.__capacidade_atual + quantidade) <= self.__capacidade_total:
            self.set_capacidade_atual(self.__capacidade_atual + quantidade)
            print(f"{quantidade} passageiros embarcaram. Capacidade atual: {self.__capacidade_atual}")
        else:
            print("Não é possível embarcar. Ônibus em movimento ou capacidade excedida.")

    def desembarcar(self, quantidade):
        if not self.__movimento and (self.__capacidade_atual - quantidade) >= 0:
            self.set_capacidade_atual(self.__capacidade_atual - quantidade)
            print(f"{quantidade} passageiros desembarcaram. Capacidade atual: {self.__capacidade_atual}")
        else:
            print("Não é possível desembarcar. Ônibus em movimento ou capacidade insuficiente.")

    def acelerar(self):
        if not self.__movimento:
            self.__movimento = True
            print("Ônibus acelerando.")
        else:
            print("Ônibus já está em movimento.")

    def frear(self):
        if self.__movimento:
            self.__movimento = False
            print("Ônibus freando.")
        else:
            print("Ônibus já está parado.")

onibus_azul = Onibus(capacidade_total=45, placa="ABC123", modelo="Volvo")
onibus_azul.embarcar(20)
onibus_azul.acelerar()
onibus_azul.embarcar(30)
onibus_azul.desembarcar(1)
onibus_azul.frear()
onibus_verde = Onibus(capacidade_total=60, placa="DFG456", modelo="FIAT")
onibus_verde.embarcar(50)
onibus_azul.acelerar()
onibus_verde.desembarcar(25)
onibus_verde.desembarcar(26)
onibus_azul.frear()

# ==========================================================================
# 2) Implemente um programa que represente uma fila. O contexto do programa é uma
# agência de banco. Cada cliente ao chegar deverá respeitar a seguinte regra: o primeiro
# a chegar deverá ser o primeiro a sair. Você poderá representar pessoas na fila a par-
# tir de números os quais representam a idade. A sua fila deverá conter os seguintes
# comportamentos:

# • Adicionar pessoa na fila: adicionar uma pessoa na fila.
# • Atender Fila: atender a pessoa respeitando a ordem de chegada
# • Dar prioridade: colocar uma pessoa maior de 65 anos como o primeiro da fila

class FilaBanco:
    def __init__(self):
        self.fila = []

    def adicionar_pessoa(self, idade):
        if idade <= 65:
            self.fila.append(idade)
        else:
            fila_banco.dar_prioridade(idade)
        print(f"Pessoa com idade {idade} adicionada à fila.")

    def atender_fila(self):
        if self.fila:
            pessoa_atendida = self.fila.pop(0)
            print(f"Atendendo pessoa com idade {pessoa_atendida}.")
        else:
            print("Fila vazia. Ninguém para atender.")

    def dar_prioridade(self, idade):
        if idade > 65:
            self.fila.insert(0, idade)
            print(f"Devido a idade de {idade} a pessoa recebeu prioridade e foi colocada no início da fila.")
        else:
            print("A pessoa não tem idade suficiente para prioridade.")

fila_banco = FilaBanco()

fila_banco.adicionar_pessoa(30)
fila_banco.adicionar_pessoa(45)
fila_banco.adicionar_pessoa(50)
fila_banco.adicionar_pessoa(70)
fila_banco.atender_fila()
fila_banco.atender_fila()
fila_banco.atender_fila()
fila_banco.atender_fila()
