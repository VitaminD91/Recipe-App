import sys
import recipeDB
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QComboBox, QCheckBox,
                             QToolTip, QMessageBox, QLabel, QVBoxLayout, QLineEdit, QWidget)
from PyQt5.QtCore import QSize

class EditIngredientWindow(QWidget):
    def __init__(self, id, ingredientUI):
        super().__init__()

        self.ingredient_id = id
        self.ingredientUI = ingredientUI
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Edit Ingredient")
        self.setGeometry(100, 100, 800, 800)

        ingredient = recipeDB.get_ingredient_by_id(self.ingredient_id)

        #create a QVBoxLayout instance
        vLayout = QVBoxLayout(self)

        nameLabel = QLabel(self)
        self.nameEdit = QLineEdit(self)
        nameLabel.setText('Name: ')
        self.nameEdit.setText(ingredient['name'])

        typeLabel = QLabel(self)
        self.typeEditCombo = QComboBox(self)
        typeList = ["Meat", "Poultry", "Pasta", "Vegetable", "Fish", "Dairy"]
        for type in typeList:
            self.typeEditCombo.addItem(type)
        typeLabel.setText('Type: ')

        DBType = ingredient['type']
        Index = typeList.index(DBType)
        self.typeEditCombo.setCurrentIndex(Index)

        vLayout.addWidget(nameLabel)
        vLayout.addWidget(self.nameEdit)

        vLayout.addWidget(typeLabel)
        vLayout.addWidget(self.typeEditCombo)            

        mainIngredient = ingredient['IsMain']
        self.isMain = QCheckBox("Main", self)
        self.isMain.setChecked(mainIngredient == 1)
        vLayout.addWidget(self.isMain)
        
        saveButton = QPushButton('Save', self)
        saveButton.clicked.connect(self.onSaveClicked)
        vLayout.addWidget(saveButton)

        cancelButton = QPushButton('Cancel', self)
        cancelButton.clicked.connect(self.onCancelClicked)
        vLayout.addWidget(cancelButton)
    
        self.resize(250, 100)
        self.show()            

    def onChanged(self, text):
        self.nameLabel.setText(text)
        self.nameLabel.adjustSize()

    def onSaveClicked(self):
        
        nameValue = str(self.nameEdit.text())
        typeValue = str(self.typeEditCombo.currentText())
        mainValue = self.isMain.isChecked()

        recipeDB.update_ingredient(self.ingredient_id, nameValue, typeValue, mainValue)
        print("Database Updated")
        self.ingredientUI.updateGrid()
        
        self.close()

    def onCancelClicked(self):
        self.close()

    


        
#if __name__ == "__main__":
#    app = QtWidgets.QApplication(sys.argv)
#    mainWin = MainWindow()
#    mainWin.show()
#    sys.exit( app.exec_() )


