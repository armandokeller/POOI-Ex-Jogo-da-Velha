from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

from modelo import Jogador, ContextoJogo


class JogoDaVelha:

    def __init__ (self):
        self._interface :QtWidgets.QWidget = None
        self._contexto = ContextoJogo()

    @property
    def interface(self)->QtWidgets.QWidget:
        return self._interface

    @interface.setter
    def interface(self, interface: str):
        loader = QUiLoader()
        self._interface = loader.load(interface, None)
        self._atribui_comandos_botoes_jogo()
        self._interface.label_mensagens.setText("Pressione Iniciar para começar.")
        self._interface.show()


    def reseta_jogo(self):
        self._reseta_interface()
        self._contexto.reset_jogo()
        self.loop_jogo()
    

    def termina_jogo(self):
        self._bloqueia_botoes()
        self._interface.label_mensagens.setText("Jogo finalizado, pressione iniciar para começar")

    def _reseta_interface(self):
        self._limpa_botoes()
        self._libera_botoes()

        self._interface.label_mensagens.setText("")

    def _bloqueia_botoes(self):
        self._interface.bt_00.setEnabled(False)
        self._interface.bt_01.setEnabled(False)
        self._interface.bt_02.setEnabled(False)
        self._interface.bt_10.setEnabled(False)
        self._interface.bt_11.setEnabled(False)
        self._interface.bt_12.setEnabled(False)
        self._interface.bt_20.setEnabled(False)
        self._interface.bt_21.setEnabled(False)
        self._interface.bt_22.setEnabled(False)

    def _limpa_botoes(self):
        self._interface.bt_00.setText(None)
        self._interface.bt_01.setText(None)
        self._interface.bt_02.setText(None)
        self._interface.bt_10.setText(None)
        self._interface.bt_11.setText(None)
        self._interface.bt_12.setText(None)
        self._interface.bt_20.setText(None)
        self._interface.bt_21.setText(None)
        self._interface.bt_22.setText(None)

    def _libera_botoes(self):
        self._interface.bt_00.setEnabled(True)
        self._interface.bt_01.setEnabled(True)
        self._interface.bt_02.setEnabled(True)
        self._interface.bt_10.setEnabled(True)
        self._interface.bt_11.setEnabled(True)
        self._interface.bt_12.setEnabled(True)
        self._interface.bt_20.setEnabled(True)
        self._interface.bt_21.setEnabled(True)
        self._interface.bt_22.setEnabled(True)

    def _atribui_comandos_botoes_jogo(self):
        self._interface.bt_00.clicked.connect(lambda x: self.clique_botao_jogo(self._interface.bt_00,(0,0)))
        self._interface.bt_01.clicked.connect(lambda x: self.clique_botao_jogo(self._interface.bt_01,(0,1)))
        self._interface.bt_02.clicked.connect(lambda x: self.clique_botao_jogo(self._interface.bt_02,(0,2)))
        self._interface.bt_10.clicked.connect(lambda x: self.clique_botao_jogo(self._interface.bt_10,(1,0)))
        self._interface.bt_11.clicked.connect(lambda x: self.clique_botao_jogo(self._interface.bt_11,(1,1)))
        self._interface.bt_12.clicked.connect(lambda x: self.clique_botao_jogo(self._interface.bt_12,(1,2)))
        self._interface.bt_20.clicked.connect(lambda x: self.clique_botao_jogo(self._interface.bt_20,(2,0)))
        self._interface.bt_21.clicked.connect(lambda x: self.clique_botao_jogo(self._interface.bt_21,(2,1)))
        self._interface.bt_22.clicked.connect(lambda x: self.clique_botao_jogo(self._interface.bt_22,(2,2)))

        self._interface.bt_iniciar.clicked.connect(self.reseta_jogo)
        self._interface.bt_terminar.clicked.connect(self.termina_jogo)
        

    def loop_jogo(self):
        if self._contexto.acabou:
            if self._contexto.ganhador is not None:
                self._interface.label_mensagens.setText(f"{self._contexto.ganhador} venceu!")
            else:
                self._interface.label_mensagens.setText("Jogo empatado")
            self._bloqueia_botoes()
        else:
            self._interface.label_mensagens.setText(f"Vez do jogador {'X' if self._contexto.jogador_atual == Jogador.XIS else 'O'}") 

    def clique_botao_jogo(self,objeto:QtWidgets.QPushButton ,posicao:tuple[int,int])->None:
        objeto.setEnabled(False)
        if self._contexto.jogador_atual == Jogador.BOLINHA:
            objeto.setText("⭕")
        else:
            objeto.setText("❌")
        self._contexto.marca_jogada(posicao[0],posicao[1])
        self.loop_jogo()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    jogo =  JogoDaVelha()
    jogo.interface  = "exemplo.ui"
    jogo.termina_jogo()
    
    app.exec()