from typing import List, Self, Optional
from core.element import Element
from core.base.style import Style
class Space:
    def __init__(self, title: str, style: Optional[Style] = None) -> None:
        self._elements: List[Element] = list()
        self.style = style or Style()
        self.title= title
    
    @property
    def elements(self):
        return self._elements

    def append(self, Element):
        self._elements.append(Element)
    
    def _wrap_with_string(self, text: str) -> str:
        return f'"{text}"'
    
    def __str__(self) -> str:
        result: str = ""
        with open(r"core\assets\templates\base.html") as f:
            text = f.read()
            result = text.replace("{$space}", f"<body {' style = ' + self._wrap_with_string(str(self.style)) if str(self.style) else ''}>{''.join([str(element) for element in self._elements])}</body>").replace("{$using pymium}", "").replace("{$title}", self.title)
            result+="""<script src="qrc:///qtwebchannel/qwebchannel.js"></script><script language="JavaScript">
        new QWebChannel(qt.webChannelTransport, function (channel) {
          window.handler = channel.objects.handler;
          handler.test(function(retVal) {
            // console.error as console.log message don't show up in the python console
            
          })
          handler.test1('pizza')
          document.getElementById('a-button').onclick = function() {
           handler.test1('pizza')
          }
        });
        
      </script>"""
        return result
