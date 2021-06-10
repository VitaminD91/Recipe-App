import sys
import recipeDB
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout, \
QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot

class RecipeUI(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 1200
        self.height = 800
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.create_grid()

        # Add box layout, add table to box layout and add box layout to widget
        #self.layout = QVBoxLayout()
        #self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.gridLayout) 

        self.SwapPageButton = QPushButton('Ingredients', self)
        self.SwapPageButton.move(100, 250)
        self.SwapPageButton.clicked.connect(self.ingredients_button_clicked)
        #Show widget
        self.show()

    def ingredients_button_clicked(self):
        print('bababooie')
        


       
    def create_grid(self):

        recipes = recipeDB.get_all_recipes()
        self.gridLayout = QGridLayout()

        boldFont = QFont()
        boldFont.setBold(True)
        
        headerLabel1 = QLabel()
        headerLabel1.setText('Name')
        headerLabel1.setFont(boldFont)
        headerLabel2 = QLabel()
        headerLabel2.setText('Time')
        headerLabel2.setFont(boldFont)
        self.gridLayout.addWidget(headerLabel1, 0,0)
        self.gridLayout.addWidget(headerLabel2, 0,1)
        


        i = 1
        for recipe in recipes:
            nameLabel = QLabel()
            nameLabel.setText(recipe['name'])
            timeLabel = QLabel()
            timeLabel.setText(recipe['Time'])
            
            self.gridLayout.addWidget(nameLabel, i, 0)
            self.gridLayout.addWidget(timeLabel, i, 1)
            i = i+1

        

    def create_table(self):
        #Create table

        recipes = recipeDB.get_all_recipes()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(recipes))
        self.tableWidget.setColumnCount(3)
        i = 0
        for recipe in recipes:
            self.tableWidget.setItem(i,0, QTableWidgetItem(recipe['name']))
            self.tableWidget.setItem(i,1, QTableWidgetItem(recipe['Time']))
            i = i+1
        self.tableWidget.move(0,0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

        

    
 
#if __name__ == '__main__':
 #   app = QApplication(sys.argv)
  #  ex = App()
   # sys.exit(app.exec_())  