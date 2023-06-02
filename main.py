from Classes import conta,HistoriContas
from datetime import datetime as dt


if __name__== "__main__":
    history = HistoriContas()

    history.setConta(conta("125254",dt.strptime("01/06/2023","%d/%m/%Y"),"001",200.0,100))
    history.setConta(conta("125254",dt.strptime("01/06/2023","%d/%m/%Y"),"002",250.0,150))
    history.setConta(conta("125254",dt.strptime("01/06/2023","%d/%m/%Y"),"003",50.0,50))