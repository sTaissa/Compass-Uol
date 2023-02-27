"""
Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente 
e ordenacaoDecrescente.

Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] 
e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].

Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método ordenacaoDecrescente.

Imprima o resultado da ordenação crescente e da ordenação decresce
[1, 2, 3, 4, 5] 
[9, 8, 7, 6]

"""
class Ordenadora():
    # construtor com lista sendo opcional 
    def __init__(self, lista=[]):
        self.__listaBaguncada = lista

    # getter da lista
    @property
    def listaBaguncada(self):
        return self.__listaBaguncada
    
    # setter da lista
    @listaBaguncada.setter
    def listaBaguncada(self, nova_lista):
        self.listaBaguncada = nova_lista

    # ordena a lista de forma crescente
    def ordenacaoCrescente(self):
        # cria nova llista para não alterar a lista bagunçada
        self.__listaCrescente = self.__listaBaguncada
        self.__listaCrescente.sort()
        return self.__listaCrescente

    # ordena a lista de forma decrescente
    def ordenacaoDecrescente(self):
        # cria nova llista para não alterar a lista bagunçada
        self.__listaDecrescente = self.__listaBaguncada
        self.__listaDecrescente.sort()
        self.__listaDecrescente.reverse()
        return self.__listaDecrescente

# testa a classe e métodos
crescente = Ordenadora([3,4,2,1,5])
decrescente = Ordenadora([9,7,6,8])
print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())