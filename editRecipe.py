import sys
import recipeDB
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QLineEdit,
                             QComboBox, QToolTip, QMessageBox, QLabel)
from PyQt5.QtCore import QSize

class EditRecipeWindow(QMainWindow):
    def __init__(self, id, recipeUI):
        super().__init__()
        
        self.recipe_id = id
        self.recipeUI = recipeUI
        self.initUI()
            
    def initUI(self):
            
        self.setWindowTitle("Edit Recipe")
        self.setGeometry(100, 100, 800, 800)

        recipe = recipeDB.get_recipe_by_id(self.recipe_id)

        vLayout = QVBoxLayout(self)

        nameLabel = QLabel(self)
        self.nameEdit = QLineEdit(self)
        nameLabel.setText('Name: ')
        self.nameEdit.setText(recipe['name'])

        timeLabel = QLabel(self)
        self.timeEditCombo = QComboBox(self)
        timeList = ["Overnight", "Long", "Medium", "Quick"]
        for time in timeList:
            self.timeEditCombo.addItem(time)
        timeLabel.setText('Time: ')
        DBTime = recipe['time']
        index = timeList.index(DBTime)
        self.timeEditCombo.setCurrentIndex(index)

        vLayout.addWidget(nameLabel)
        vLayout.addWidget(self.nameEdit)

        vLayout.addWidget(timeLabel)
        vLayout.addWidget(self.timeEditCombo)

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
        timeValue = str(self.timeEditCombo.currentText())

        recipeDB.update_recipe(self.ingredient_id, nameValue, timeValue)
        print("Database Updated")
        self.recipeUI.updateGrid()
        
        self.close()

    def onCancelClicked(self):
        self.close()



#if __name__ == "__main__":
 #   app = QApplication(sys.argv)
  #  a = EditRecipeWindow()
   # sys.exit(app.exec_())