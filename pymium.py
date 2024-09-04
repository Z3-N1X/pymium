import webview

from core.base import Types
from core.element import Element, handler
from core import Space

def run(space):
    window = webview.create_window('Transparency Test', html=str(space), transparent=True, frameless=True, width=300, height=150, on_top=True)
    webview.start()
