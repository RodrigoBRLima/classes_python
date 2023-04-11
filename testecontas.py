from contas import Conta
from cliente import Cliente

cliente1 = Cliente(123,"João", "Rua 1")
cliente2 = Cliente(345,'Maria',"Rua 2")

conta1 = Conta([cliente1,cliente2],1,0) #agregação - vou passar os dois objetos criados e instanciados para a classe Conta

conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()
