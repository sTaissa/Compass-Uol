"""
Crie uma classe chamada "Pessoa" com um atributo privado "nome" (representado como "__nome") e um atributo público 
"id". Adicione duas funções à classe, uma para definir o valor de "nome" e outra para obter o valor de "nome". 
Observe que o atributo "nome" deve ser privado e acessado somente através dessas funções.

Para testar seu código use:
pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)

"""
class Pessoa():

    # construtor com id sendo passado e nome opcional
    def __init__(self, id, nome=""):
        self.id = id
        self.__nome = nome
    
    # função que permite obter o valor da propriedade privada nome
    @property
    def nome(self):
        return self.__nome

    # função que permite alterar o valor da propriedade privada nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

# testando a classe nos parâmetros pedidos
pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)