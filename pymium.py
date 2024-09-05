# import webview

from core.base import Types
from core.element import Element, handler
from core.base.style import Style
from core import Space



from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore
import sys
import os

class _MainWindow(QMainWindow):
    def __init__(self, space: Space, title: str, width: int = 800, height: int = 600, frameless: bool = False, on_top: bool = False):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        view = QtWebEngineWidgets.QWebEngineView()
        html = str(space)
        view.setHtml(html)
        self.setWindowFlags(
            self.windowFlags() 
            | QtCore.Qt.FramelessWindowHint if frameless else self.windowFlags() 
            | QtCore.Qt.WindowStaysOnTopHint if on_top else self.windowFlags() 
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        
        # self.setWindowOpacity(0.5)
        self.setCentralWidget(view)




def run(space:Space, width: int = 800, height: int = 600, always_on_top: bool = False, frameless: bool= False):
    app = QApplication(sys.argv)


    window = _MainWindow(space, space.title, width, height, frameless, always_on_top)
    window.show()


    app.exec()