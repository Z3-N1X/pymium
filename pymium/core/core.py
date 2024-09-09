from typing import List, Self, Optional
from pymium.core.element import Element
from pymium.core.base.style import Style
from pymium.core.assets.templates import templates
class Space:
    def __init__(self, title: str, style: Optional[Style] = None) -> None:
        self._elements: List[Element] = list()
        self.style = style or Style()
        self.title = title
        self._custom_style = ""
    
    @property
    def elements(self):
        return self._elements

    def append(self, Element):
        self._elements.append(Element)
    
    def _wrap_with_string(self, text: str) -> str:
        return f'"{text}"'
    
    def add_custom_css(self, css: str):
        self._custom_style += css

    def __str__(self) -> str:
        result: str = ""
        text = templates.base_html
        result = text.replace("{$space}", f"<body {' style = ' + self._wrap_with_string(str(self.style)) if str(self.style) else ''}>{'<style>'+ self._custom_style + '</style>' if self._custom_style else ''}{''.join([str(element) for element in self._elements])}</body>").replace("{$using pymium}", "").replace("{$title}", self.title)
        
        return result
