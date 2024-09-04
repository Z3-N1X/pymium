import webview

from core.base import Types
from core.element import Element, handler
from core.base.style import Style
from core import Space

def run(space:Space, width: int = 800, height: int = 600, always_on_top: bool = False, transparent: bool = False, frameless: bool= False):
    window = webview.create_window(space.title, html=str(space), transparent=transparent, frameless=frameless, width=width, height=height, on_top=always_on_top)
    webview.start()
