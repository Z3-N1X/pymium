# import webview
# window = webview.create_window('Woah dude!', 'test.html')
# webview.start(custom_logic, window)


from core.base import Type
from core.element.element import Element

print(Element(
    Type("div"),
    className="hi"
))

