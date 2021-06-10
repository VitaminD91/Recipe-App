import sys
import recipeDB
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QPushButton, QTableWidget,QTableWidgetItem,QVBoxLayout, QGridLayout, QLabel, QGroupBox, QHBoxLayout
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
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.create_grid()
        

        self.show()

        # Add box layout, add table to box layout and add box layout to widget
       # self.layout = QVBoxLayout()
       # self.layout.addWidget(self.gridLayout) 
        self.setLayout(self.gridLayout) 

        #Show widget
        self.show()
        

    def create_table(self):
        #Create table

        ingredients = recipeDB.get_all_ingredients()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(ingredients))
        self.tableWidget.setColumnCount(4)
        i = 0
        for ingredient in ingredients:
            self.tableWidget.setItem(i,0, QTableWidgetItem(ingredient['name']))
            self.tableWidget.setItem(i,1, QTableWidgetItem(ingredient['type']))
            self.tableWidget.setItem(i,2, QTableWidgetItem(str(ingredient['IsMain'])))
            i = i+1
        self.tableWidget.move(0,0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)


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



    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    @pyqtSlot()
    def on_edit_click(self, id):
        print(id)

    @pyqtSlot()
    def on_delete_click(self, id):
        print(id)

#if __name__ == '__main__':
    #app = QApplication(sys.argv)
    #ex = App()
    #sys.exit(app.exec_())  