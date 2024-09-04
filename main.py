# import webview

# window = webview.create_window('Transparency Test', "file.html", transparent=True, frameless=True, width=300, height=150, on_top=True)
# webview.start()
from core.base import Types
from core.element import Element, handler
from core import Space


def start():
    aDiv = Element(Types.div, "E")
    nDiv = Element(Types.h1, "N")
    space = Space("Main")
    space.append(aDiv)
    aDiv.append(nDiv)
    print(str(space))

start()
