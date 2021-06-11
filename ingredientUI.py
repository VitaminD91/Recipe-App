import sys
import recipeDB
import editIngredient as eI
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QPushButton, QTableWidget,QTableWidgetItem,QVBoxLayout, QGridLayout, QLabel, QGroupBox, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot

class IngredientUI(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Ingredients'
        self.left = 0
        self.top = 0
        self.width = 1200
        self.height = 800
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.initUI()
        
    def initUI(self):
        
        
        self.create_grid()
        self.show()

        # Add box layout, add table to box layout and add box layout to widget
       # self.layout = QVBoxLayout()
       # self.layout.addWidget(self.gridLayout) 
        self.setLayout(self.gridLayout) 

        #Show widget
        self.show()

    def create_grid(self):
            #Create grid

        ingredients = recipeDB.get_all_ingredients()
        self.gridLayout = QGridLayout()

        #create bold font
        boldFont = QFont()
        boldFont.setBold(True)
        #assign labels and set font
        headerLabel1 = QLabel()
        headerLabel1.setText('Name')
        headerLabel1.setFont(boldFont)
        headerLabel2 = QLabel()
        headerLabel2.setText('Type')
        headerLabel2.setFont(boldFont)
        headerLabel3 = QLabel()
        headerLabel3.setText('Main')
        headerLabel3.setFont(boldFont)
        self.gridLayout.addWidget(headerLabel1, 0,0)
        self.gridLayout.addWidget(headerLabel2, 0,1)
        self.gridLayout.addWidget(headerLabel3, 0,2)
        addButton = QPushButton('Add', self)
        self.gridLayout.addWidget(addButton, 5, 5)
        
        #populate grid
        i = 1
        for ingredient in ingredients:
            nameLabel = QLabel()
            nameLabel.setText(ingredient['name'])
            typeLabel = QLabel()
            typeLabel.setText(ingredient['type'])
            mainLabel = QLabel()
            mainLabel.setText(str(ingredient['isMain']))
            
            self.boxesLayout(ingredient['id'])
            self.gridLayout.addWidget(nameLabel, i, 0)
            self.gridLayout.addWidget(typeLabel, i, 1)
            self.gridLayout.addWidget(mainLabel, i, 2)
            self.gridLayout.addWidget(self.horizontalGroupBox, i, 3)
            i = i+1
    
    def boxesLayout(self, id):
        self.horizontalGroupBox = QGroupBox()
        layout = QHBoxLayout()

        editButton = QPushButton('Edit', self)
        editButton.clicked.connect(lambda: self.on_edit_click(id))
        layout.addWidget(editButton)

        deleteButton = QPushButton('Delete', self)
        deleteButton.clicked.connect(lambda: self.on_delete_click(id))
        layout.addWidget(deleteButton)

        self.horizontalGroupBox.setLayout(layout)

    def updateGrid(self):
        QWidget().setLayout(self.layout())
        self.initUI() 

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    @pyqtSlot()
    def on_edit_click(self, id):
        self.a = eI.EditIngredientWindow(id, self) 
    
    def on_delete_confirm_clicked(self, val, id):
        if val == "&Yes":
            recipeDB.delete_ingredient(id)
            self.updateGrid()
            print("deleting...")
            
            

    @pyqtSlot()
    def on_delete_click(self, id):
        
        msg = QMessageBox()
        msg.setInformativeText("Are you Sure?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.buttonClicked.connect(lambda val: self.on_delete_confirm_clicked(val.text(), id))
        x = msg.exec_()
    

#if __name__ == '__main__':
    #app = QApplication(sys.argv)
    #ex = App()
    #sys.exit(app.exec_())  