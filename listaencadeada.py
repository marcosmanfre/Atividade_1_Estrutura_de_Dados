from no import Node

class LinkedList:
    def __init__(self):
        self.inicio = None
        self._tamanho = 0


    def __len__(self):
        return self._tamanho

       
    def append(self, info):
        if self.inicio:
            aux = self.inicio
            while(aux.proximo):
                aux = aux.proximo
            aux.proximo = Node(info)
        else:
            self.inicio = Node(info)
        self._tamanho += 1
    
    def __getitem__(self, index):
        aux = self._getNo(index)
        if aux:
            return aux.info
        else:
            raise IndexError('Índice não existente!')

    def __setitem__(self, index, info):
        aux = self._getNo(index)
        if aux:
            aux.info = info
        else:
            raise IndexError('Índice não existente!')

    def _getNo(self, index):
        aux = self.inicio
        for i in range(index):
            if aux:
                aux = aux.proximo
            else:
                return None
        return aux


    def __repr__(self):
        r = ""
        aux = self.inicio
        while(aux):
            r = r + str(aux.info) + "->"
            aux = aux.proximo
        return r
    
    def __str__(self):
        return self.__repr__()