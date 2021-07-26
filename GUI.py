import functools
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QDateTimeEdit


app = QApplication([])

window = QWidget()
window.setWindowTitle('Handicap Display')

buttons = []

afterSelected = False
beforeSelected = False

def buttonPress(button):
    for btn in buttons:
        btn.setDown(False)
    button.setDown(True)

def afterButtonPressed(button):
    global afterSelected
    afterSelected = not afterSelected
    button.setDown(afterSelected)

def beforeButtonPressed(button):
    global beforeSelected
    beforeSelected = not beforeSelected
    button.setDown(beforeSelected)




layoutDaySelect = QGridLayout()
layoutTimeSelect = QGridLayout()
layoutTimeSelectAfter = QGridLayout()
layoutTimeSelectBefore = QGridLayout()
mainLayout = QGridLayout()

for i in range(0, 7):
    new_button = QPushButton(str(i))
    new_button.clicked.connect(functools.partial(buttonPress, new_button))
    layoutDaySelect.addWidget(new_button, 0, i)
    buttons.append(new_button)

afterButton = QPushButton('After')
afterButton.clicked.connect(functools.partial(afterButtonPressed, afterButton))
layoutTimeSelectAfter.addWidget(afterButton, 0, 0)
afterTimeSelect = QDateTimeEdit()
layoutTimeSelectAfter.addWidget(afterTimeSelect, 1, 0)

beforeButton = QPushButton('Before')
beforeButton.clicked.connect(functools.partial(beforeButtonPressed, beforeButton))
layoutTimeSelectBefore.addWidget(beforeButton)


layoutTimeSelect.addLayout(layoutTimeSelectAfter, 0, 0)
layoutTimeSelect.addLayout(layoutTimeSelectBefore, 0, 1)

mainLayout.addLayout(layoutDaySelect, 0, 0)
mainLayout.addLayout(layoutTimeSelect, 1, 0)


window.setLayout(mainLayout)
buttons[0].setDown(True)
print(buttons[0].isDown())




window.show()
sys.exit(app.exec_())