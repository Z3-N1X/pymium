# import webview
# window = webview.create_window('Woah dude!', 'test.html')
# webview.start(custom_logic, window)


from core.base import Type
from core.element import Element, handler
from core import Space


def start():
    aDiv = Element(Type("div"), "E")
    nDiv = Element(Type("div"), "N")
    space = Space()
    space.append(aDiv)
    aDiv.append(nDiv)
    print([x.id for x in aDiv.childs])

start()
