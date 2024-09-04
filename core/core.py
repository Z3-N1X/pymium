from typing import List, Self, Optional
from core.element import Element
class Space:
    def __init__(self, title: str) -> None:
        self._elements: List[Element] = list()
        self.title= title
    
    @property
    def elements(self):
        return self._elements

    def append(self, Element):
        self._elements.append(Element)
    
    def __str__(self) -> str:
        result: str = ""
        with open(r"core\assets\templates\base.html") as f:
            text = f.read()
            result = text.replace("{$space}", f"<body>{''.join([str(element) for element in self._elements])}</body>").replace("{$using pymium}", "").replace("{$title}", self.title)
        return result
