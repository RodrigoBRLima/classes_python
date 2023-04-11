class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir(self):
        print(self.nome, " tem ", self.idade, " ano(s)")

    def getIdade(self):
        return self.idade

    def setIdade(self,idade):
        self.idade = idade


#herança
class Profissional(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao

    def imprimir(self):
        super().imprimir()
        print('\t e trabalha como ', self.profissao)


p = Profissional("Ana",25,'balconista')
p.imprimir()