"""
Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.
Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.
Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.
Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:
“O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.
Sendo x, y, z e w cada um dos atributos da classe “Avião”.

Valores de entrada:
modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul
modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul
modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul

"""
class Aviao():
    # atributo de classe, todas as instancias tem com esse mesmo valor
    cor = "azul"

    # construtor
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.__modelo = modelo
        self.__velocidade_maxima = velocidade_maxima
        self.__capacidade = capacidade
    
    #getters e setter dos atributos
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, novo_modelo):
        self.modelo = novo_modelo

    @property
    def velocidade_maxima(self):
        return self.__velocidade_maxima
    
    @velocidade_maxima.setter
    def velocidade_maxima(self, nova_velocidade):
        self.velocidade_maxima = nova_velocidade
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, nova_capacidade):
        self.capacidade = nova_capacidade

# cria uma lista com 3 objetos da classe Aviao
lista = []
lista.append(Aviao("BOIENG456", "1500 km/h", "400"))
lista.append(Aviao("Embraer Praetor 600", "863km/h", "14"))
lista.append(Aviao("Antonov An-2", "258 Km/h", "12"))

# exibe os valores de cada objeto
for i in lista:
    print(f"O avião de modelo {i.modelo} possui uma velocidade máxima de {i.velocidade_maxima}, capacidade para {i.capacidade} passageiros e é da cor {Aviao.cor}")