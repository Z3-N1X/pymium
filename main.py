# import webview
# window = webview.create_window('Woah dude!', 'test.html')
# webview.start(custom_logic, window)


from core.base import Type
from core.element import Element
from core import Space


def start():
    aDiv = Element(Type("div"), "E")
    space = Space()
    space.append(aDiv)
    print(space.elements)

start()
