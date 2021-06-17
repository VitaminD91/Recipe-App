import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class DashUI(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Dashboard'
        self.left = 0
        self.top = 0
        self.width = 1200
        self.height = 800
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.initUI()
        
    def initUI(self):
        
        self.create_grid()
        #Show widget
        self.show()
        self.setLayout(self.gridLayout)
        self.show()
    
    def weekdays(day):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        i=days.index(day)
        week=days[i:] 
        week.extend(days[:i])
        return week
    
    def create_grid(self):
        
        
        weekList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                    "Saturday", "Sunday"]
            

        boldFont = QFont()
        boldFont.setBold(True)
        self.gridLayout = QGridLayout()

        i = 0
        
        for day in weekList:
            dayLabel = QLabel()
            dayLabel.setText(weekList[0 + i])
            dayLabel.setFont(boldFont)
            dayLabel.setAlignment(Qt.AlignCenter)
            dayLabel.setStyleSheet("QLabel {background-color: lightgrey;}")
            self.gridLayout.addWidget(dayLabel, 0, i)
            swapButton = QPushButton('Swap', self)
            self.gridLayout.addWidget(swapButton, 2, i)
            i = i+1


#if __name__ == "__main__":
 #   DashUI = QApplication(sys.argv)
  #  mainWin = DashUI()
   # sys.exit(DashUI.exec_())