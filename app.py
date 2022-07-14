# para usar o pyQT é necessário fazer sua instalação
# pip install pyqt5
# para ajudar no preenchimento também instale o 'PyQt5-stubs==5.15.6.0'

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora BRABA')  # nome da aplicação
        self.setFixedSize(500, 500)  # determina o tamanho da aplicação, porém não se pode redimensionar
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)  # com isso determina que o Display onde vai aparecer os números eu só posso ver e não posso escrever nada nele
        self.display.setStyleSheet('* {background: #FFF; color: #000; font-size: 50px;}')  # igual CSS
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # determinar que ele siga o padrão da janela

        #adicionando botões -- primeira linha (superior)
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(QPushButton('C'), 1, 4, 1, 1,
                     lambda: self.display.setText(''),
                     'background: #d5580d; color: #fff; font-weight: 700;')  # Botão Clear

        # adicionando botões -- segunda linha
        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(QPushButton('<-'), 2, 4, 1, 1, lambda: self.display.setText(self.display.text()[:-1]),
                     'background: #cd2d2d; color: #fff; font-weight: 700;')  # Apaga um caractere

        # adicionando botões -- terceira linha
        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        # self.add_btn(QPushButton(''), 3, 4, 1, 1)

        # adicionando botões -- quarta linha
        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(QPushButton('='), 4, 4, 1, 1, self.eval_igual,
                     'background: #13823a; color: #fff; font-weight: 700;')

        self.setCentralWidget(self.cw)

    # trabalhando com os botões da calculadora
    def add_btn(self, btn, row, col, rowspan, colspan, func=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not func:
            btn.clicked.connect(lambda: self.display.setText(self.display.text() + btn.text()))
        else:
            btn.clicked.connect(func)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    # método de pegar o resultado (IGUAL)
    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))  # eval já entende os caracteres e faz a conta
        except Exception as e:
            self.display.setText('Conta Inválida')
            print("ERROR:", e)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Calculadora()
    app.show()
    qt.exec_()
