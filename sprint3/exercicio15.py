"""
Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, True se a lâmpada estiver 
ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:

liga(): muda o estado da lâmpada para ligada
desliga(): muda o estado da lâmpada para desligada
esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

Para testar sua classe:

Ligue a Lampada
Imprima: A lâmpada está ligada? True
Desligue a Lampada
Imprima: A lâmpada ainda está ligada? False

"""
class Lampada():
    ligada = False

    # construtor
    def __init__(self, ligada):
        self._ligada = ligada

    # liga a lâmpada se estiver desligada
    def liga(self):
        if self._ligada == False:
            self._ligada = True
    
    # delisga a lâmapda se estiver ligada
    def desliga(self):
        if self._ligada == True:
            self._ligada = False
    
    # verifica se a lâmpada está ligada, retorna True se estiver e False se não
    def esta_ligada(self):
        if self._ligada == True:
            return True
        else:
            return False

# cria a classe lâmpada e testa seus métodos
lamp = Lampada(True)

lamp.liga()

print("A lâmpada está ligada? " + str(lamp.esta_ligada()))

lamp.desliga()

print("A lâmpada ainda está ligada? " + str(lamp.esta_ligada()))
        