from abc import ABC, abstractmethod

class VOO(ABC):

    def __init__(self, empresa, dataorigem, siglaorigem, horaorigem, cidadeorigem, aeroportoorigem, dataconex, siglaconex, horaconex, cidadeconex, aeroportoconex, duracao, classe, observacao):
        self.__empresa = empresa
        self.__dataorigem = dataorigem
        self.__siglaorigem = siglaorigem
        self.__horaorigem = horaorigem
        self.__cidadeorigem = cidadeorigem
        self.__aeroportoorigem = aeroportoorigem
        self.__dataconex = dataconex
        self.__siglaconex = siglaconex
        self.__horaconex = horaconex
        self.__cidadeconex = cidadeconex
        self.__aeroportoconex = aeroportoconex
        self.__duracao = duracao
        self.__classe = classe
        self.__observacao = observacao


    def getEmpresa(self):
        return self.__empresa

    def setEmpresa(self, empresa):
        self.__empresa = empresa

    def getDataorigem(self):
        return self.__dataorigem

    def setDataorigem(self, dataorigem):
        self.__dataorigem = dataorigem

    def getSiglaorigem(self):
        return self.__siglaorigem

    def setSiglaorigem(self, siglaorigem):
        self.__siglaorigem = siglaorigem

    def getHoraorigem(self):
        return self.__horaorigem

    def setHoraorigem(self, horaorigem):
        self.__horaorigem = horaorigem

    def getCidadeorigem(self):
        return self.__cidadeorigem

    def setCidadeorigem(self, cidadeorigem):
        self.__cidadeorigem = cidadeorigem

    def getAeroportoorigem(self):
        return self.__aeroportoorigem

    def setAeropostoorigem(self, aeroportoorigem):
        self.__aeroportoorigem = aeroportoorigem

    def getDataconex(self):
        return self.__dataconex

    def setDataconex(self, dataconex):
        self.__dataconex = dataconex

    def getSiglaconex(self):
        return self.__siglaconex

    def setSiglaconex(self, siglaconex):
        self.__siglaconex = siglaconex

    def getHoraconex(self):
        return self.__horaconex

    def setHoraconex(self, horaconex):
        self.__horaconex = horaconex

    def getCidadeconex(self):
        return self.__cidadeconex

    def setCidadeconex(self, cidadeconex):
        self.__cidadeconex = cidadeconex

    def getAeropostoconex(self):
        return self.__aeroportoconex

    def setAeropostoconex(self, aeroportoconex):
        self.__aeroportoconex = aeroportoconex

    def getDuracao(self):
        return self.__duracao

    def setDuracao(self, duracao):
        self.__duracao = duracao

    def getClasse(self):
        return self.__classe

    def setClasse(self, classe):
        self.__classe = classe

    def getObservacao(self):
        return self.__observacao

    def setObvervacao(self, observacao):
        self.__observacao = observacao

        

    def __str__(self):
        return "Empresa: " + self.__empresa + "Data: " + str(self.__dataorigem) + "Sigla: " + str(self.__siglaorigem + "Hora: " + str(self.__horaorigem) + "Cidade: " + str(self.__cidadeorigem) + "Aeroporto: " + str(self.__aeroportoorigem) + "Data Conexão: " + str(self.__dataconex) + "Sigla Conexão: " + str(self.__siglaconex) + "Hora Conexão: " + str(self.__horaconex) + "Cidade Conexão: " + str(self.__cidadeconex) + "Aeroporto Conexão: " + str(self.__aeroportoconex) + "Duração: " + str(self.__duracao) + "Classe: " + str(self.__classe) + "Observação: " + str(self.__observacao))