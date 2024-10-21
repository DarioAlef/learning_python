import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QtCore, QMainWindow, QTableWidgetItem, QLabel, QLineEdit, QTableWidget, QVBoxLayout, QWidget, QSpacerItem, QPushButton

class MainForm(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        
        self.label_nome = QLabel()
        self.label_nome.setText('Nome')
        
        self.edt_nome = QLineEdit()
        
        self.button_adicionar = QPushButton('Adicionar')
        self.button_adicionar.clicked.connect(self.clicando)
        
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Nome', 'Sexo'])
        self.table.setRowCount(0)
        
        space = QSpacerItem(0, 65, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.label_nome)
        vertical_layout.addWidget(self.edt_nome)
        vertical_layout.addWidget(self.button_adicionar)
        vertical_layout.addWidget(self.table)
        vertical_layout.addItem(space)
        
        self.componentes = QWidget()
        self.componentes.setLayout(vertical_layout)
        
        
        
        self.setCentralWidget(self.componentes)
        
        self.setWindowTitle('Minha primeira tela: Hello World!')
        self.setGeometry(10, 10, 600, 400)
        
    def clicando(self):
        print('\nCliquei no botão \"Adicionar\"!\n')
        
    def popular_tabela(self):
        self.table.setRowCount(len(self.FUNCIONATIOS))
        for linha, valor in enumerate(self.FUNCIONATIOS):
            nome = QTableWidgetItem()
            nome.setText(valor['nome'])
            nome.setData(QtCore.Qt.UserRole, valor['id'])
            
            sexo = QTableWidgetItem()
            sexo.setText(valor['sexo'])
            
            self.table.setItem(linha, 0, nome)
            self.table.setItem(linha, 1, sexo)
        
if __name__ == '__main__':        
    app = QApplication(sys.argv)
    main = MainForm()
    main.show()
    sys.exit(app.exec_())