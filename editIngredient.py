import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel)

class EditIngredientWindow(QMainWindow):
    def __init__(self):
            super().__init__()
            self.setWindowTitle("Edit Ingredient")

            self.setGeometry(100, 100, 800, 800)

            self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = EditIngredientWindow()
    sys.exit(app.exec_())  