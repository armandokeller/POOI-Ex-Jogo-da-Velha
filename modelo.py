from enum import IntEnum

class Jogador(IntEnum):
        XIS = 1
        BOLINHA = 2

class ContextoJogo:

    def __init__(self) -> None:
        self.reset_jogo()
    
    @property
    def jogador_atual(self):
        return self._jogador_atual
    
    @property
    def ganhador(self):
        if self._ganhador == Jogador.BOLINHA:
            return "Bolinha"
        elif self._ganhador == Jogador.XIS:
            return "Xis"
        return None
    
    @property
    def acabou(self)->bool:
        return self._qnt_jogadas==9 or self._ganhador is not None
    

    def marca_jogada(self, pos_x:int, pos_y: int)->None:
        self._matriz_resultados[pos_x][pos_y] =  self._jogador_atual
        self._qnt_jogadas += 1
        self.alterna_jogador()
        self.verifica_ganhador()

    def alterna_jogador(self):
        match self._jogador_atual:
            case Jogador.XIS:
                self._jogador_atual =  Jogador.BOLINHA
            case Jogador.BOLINHA:
                self._jogador_atual =  Jogador.XIS
            case _:
                self._jogador_atual = Jogador.XIS

    def verifica_ganhador(self)->bool:
        self._ganhador =  None
        if self._verifica_diagonal_principal() or self._verifica_diagonal_inversa():
            self._ganhador =  self._matriz_resultados[1][1]
        for indice in range(3):
           if self._verifica_linha(indice):
               self._ganhador =  self._matriz_resultados[indice][0]
               break
           if self._verifica_coluna(indice):
                self._ganhador =  self._matriz_resultados[0][indice]
                break
        return (self._ganhador is not None)


    def _confere_resultado(self, lista:list[int])->bool:
        if 0<lista[0]<3:
            return lista[1]==lista[0] and lista[2]==lista[0]
        return False
    
    def _verifica_coluna(self, coluna:int)->bool:
        valores  = []
        if 0<=coluna<=2:
            for linha in range(3):
                valores.append(self._matriz_resultados[linha][coluna])
            return self._confere_resultado(valores)
        return False
    
    def _verifica_linha(self, linha:int)->bool:
        if 0<=linha<=2:
            return self._confere_resultado(self._matriz_resultados[linha])
        return False
    
    def _verifica_diagonal_principal(self)->bool:
        valores = []
        for indice in range(3):
            valores.append(self._matriz_resultados[indice][indice])
        return self._confere_resultado(valores)
    
    def _verifica_diagonal_inversa(self)->bool:
        valores = []
        for indice in range(3):
            valores.append(self._matriz_resultados[indice][2-indice])
        return self._confere_resultado(valores)

    def reset_jogo(self):
        self._qnt_jogadas:int = 0
        self._jogador_atual:Jogador =  Jogador.XIS
        self._matriz_resultados = [[0,0,0],[0,0,0],[0,0,0]]
        self._ganhador:Jogador = None
