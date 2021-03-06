import sys
import ingredientUI as iUI
import recipeUI as rUI
import dashUI as dUI
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Recipe App'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
    
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.dashTab = QWidget()
        self.recipeTab = QWidget()
        self.ingredientTab = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.dashTab,"Dashboard")
        self.tabs.addTab(self.recipeTab,"Recipes")
        self.tabs.addTab(self.ingredientTab,"Ingredients")
        
        # Create Dashboard tab
        self.dashTab.layout = QVBoxLayout(self)
        self.dashTab.layout.addWidget(dUI.DashUI())
        self.dashTab.setLayout(self.dashTab.layout)

        # Create ingredient tab
        self.ingredientTab.layout = QVBoxLayout(self)
        self.ingredientTab.layout.addWidget(iUI.IngredientUI())
        self.ingredientTab.setLayout(self.ingredientTab.layout)

        # Create recipe tab
        self.recipeTab.layout = QVBoxLayout(self)
        self.recipeTab.layout.addWidget(rUI.RecipeUI())
        self.recipeTab.setLayout(self.recipeTab.layout)
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
        self.show()
        
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())