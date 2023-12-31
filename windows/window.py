from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QLineEdit

# documentation window for supported languages for CubeScript

class DocumentationWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("CubeScript Documentation")
        self.setWindowIcon(QtWidgets.QIcon("icons/cubescript.png"))
        self.setMinimumSize(500, 500)
        self.setMaximumSize(500, 500)
        self.setStyleSheet("background-color: #1a1a1a; color: #ffffff;")
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        self.textbox = QtWidgets.QTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.setStyleSheet("background-color: #1a1a1a; color: #ffffff;")

        self.setCentralWidget(self.textbox)

        self.textbox.setText("CubeScript is a simple scripting language that is used by the Cube Engine. It is used to control the game engine and to create game logic. It is a simple language that is easy to learn, but it is also very powerful. CubeScript is a stack-based language, which means that it uses a stack to store and retrieve data. CubeScript is also a dynamically typed language, which means that variables do not have a type, and that the type of a variable can change at any time. CubeScript is also a whitespace-sensitive language, which means that indentation is important. CubeScript is also a case-sensitive language, which means that uppercase and lowercase letters are treated as different characters. CubeScript also supports comments, which are ignored by the interpreter. Comments start with a # character and end at the end of the line. CubeScript also supports strings, which are sequences of characters surrounded by double quotes.")
        self.textbox.moveCursor(QtWidgets.QTextCursor.Start)

        self.show()