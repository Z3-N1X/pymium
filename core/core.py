from typing import List, Self, Optional
from core.element import Element
class Space:
    def __init__(self) -> None:
        self._elements: List[Element] = list()
    
    @property
    def elements(self):
        return self._elements

    def append(self, Element):
        self._elements.append(Element)
