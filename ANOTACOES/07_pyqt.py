import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__(parent=parent)
        
        self.setWindowTitle('Minha primeira tela: Hello World!')
        self.setGeometry(20, 20, 800, 400)
        
app = QApplication(sys.argv)
main = MainForm()
main.show()
sys.exit(app.exec_())