from datetime import datetime
import datetime as dt
class conta: 
    def __init__(self,n_conta:str="",dataleitura:datetime=datetime.now(),nleitura:str="",valor:float=0,kwgasto:int=0)-> None:
        self.__n_conta = n_conta
        self.__data_leitura = dataleitura
        self.__n_leitura = nleitura
        self.__valor_pagar = valor
        self.__data_pgto = dt.timedelta(days=20)+datetime.now()
        self.__kwGasto = kwgasto

    def getDataLeitura(self) -> str:
        return self.__data_leitura.strftime(" %d %m %Y ")
    def getKwgasto(self)-> int:
        return self.__kwGasto
    def getValorGasto(self)-> float:
        return self.__valor_pagar
    def getDadosConta(self):
        pass




    
                 
                 