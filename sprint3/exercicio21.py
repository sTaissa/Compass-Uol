"""
Implemente duas classes Pato e Pardal que herdem de uma classe Passaro a habilidade de voar e emitir som, porém, 
tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console.

Imprima no console exatamente assim:

Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu
"""
# classe passaro voa e emite som
class Passaro():
    def voa(self):
        print("Voando...")

    def emite_som(self):
        print("Passaro emitindo som...")

# classe pato tem nome, herda voo da classe passaro e emite som diferente
class Pato(Passaro):
    _nome = "Pato"

    def emite_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")

    @property
    def nome(self):
        return self._nome

# classe pardal tem nome, herda voo da classe passaro e emite som diferente
class Pardal(Passaro):
    _nome = "Pardal"

    def emite_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")

    @property
    def nome(self):
        return self._nome

# testa classes
pato = Pato()
pardal = Pardal()

print(pato.nome)
pato.voa()
pato.emite_som()

print(pardal.nome)
pardal.voa()
pardal.emite_som()