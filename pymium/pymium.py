# import webview

from pymium.core.base import Types
from pymium.core.element import Element, handler
from pymium.core.base.style import Style
from pymium.core import Space



from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSlot, QVariant
from PyQt5.QtWebChannel import QWebChannel
import sys



class PymiumWindow(QMainWindow):
    def __init__(self, space: Space, title: str, width: int = 800, height: int = 600, frameless: bool = False, on_top: bool = False):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.view = QtWebEngineWidgets.QWebEngineView()
        html = str(space)
        self.view.setHtml(html)

        self.setWindowFlags(
            self.windowFlags() 
            | QtCore.Qt.FramelessWindowHint if frameless else self.windowFlags() 
            | QtCore.Qt.WindowStaysOnTopHint if on_top else self.windowFlags() 
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.channel = QWebChannel()
        self.handler = CallHandler(space)
        self.channel.registerObject('handler', self.handler)
        self.view.page().setWebChannel(self.channel)
        # self.setWindowOpacity(0.5)
        self.setCentralWidget(self.view)
    def reload_html(self, space:Space):
        self.view.setHtml(str(space))


class CallHandler(QObject):
    def __init__(self, space: Space):
        super().__init__()
        self.space=space
    
    @pyqtSlot(QVariant, result=QVariant)
    def test1(self, args):
        element_data = str(args).split(":")
        element_name = element_data[0]
        element_id = element_data[1]    if element_data[2]!="noId" else None
        element_class = element_data[2] if element_data[2]!="noClass" else None

        id_elements = handler.getElementById(self.space, element_id)

        targets = []

        for element in id_elements:
          if element.className == element_class and str(element.elementType) == element_name:
            targets.append(element)

        for element in targets: 
            if element.onclick.__code__.co_argcount > 0:
                element.onclick(element)
            else:
                element.onclick()
        return "ok"

class PyWindow:
    def __init__(self, space:Space, width: int = 800, height: int = 600, always_on_top: bool = False, frameless: bool= False):
        self.app = QApplication(sys.argv)


        self.window = PymiumWindow(space, space.title, width, height, frameless, always_on_top)

    def run(self):
        
        self.window.show()


        self.app.exec()

    def set_html(self,space):
        self.window.reload_html(space) 
