import webview

from pymium.base import Types
from pymium.element import Element, handler
from pymium.base.style import Style
from pymium import Space

def run(space:Space, width: int = 800, height: int = 600, always_on_top: bool = False, transparent: bool = False, frameless: bool= False):
    window = webview.create_window(space.title, html=str(space), transparent=transparent, frameless=frameless, width=width, height=height, on_top=always_on_top)
    webview.start()
