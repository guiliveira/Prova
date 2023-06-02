from .conta import conta
class HistoriContas:
    def __init__(self) -> None:
        self.__contas = []

    def getMediaKw(self):
        pass
    def getValorMediaContas(self):
        pass
    def getMesMaiorConsumo(self):
        pass
    def getMesMenorConsumo(self):
        pass
    def setConta(self,conta:conta):
        self.__contas.append(conta)


