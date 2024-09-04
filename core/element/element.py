from core.base import Type
from typing import Optional, Self

class Element:
    def __init__(self,
                 elementType: Type,
                 id: Optional[str] = None,
                 className: Optional[str] = None,
                 innerHTML: Optional[str] = None,
                 parent: Optional[Self] = None
                 ):
        self.elementType = elementType
        self.id = id
        self.className = className
        self.innerHTML = innerHTML
        self._parent = parent
        self._childs: list[Self] = []

    @property
    def parent(self) -> Optional[Self]:
        return self._parent
    
    @parent.setter
    def parent(self, parent:Self):
        self._parent = parent

    @property
    def childs(self) -> list[Self]:
        return self._childs
    
    def append(self, *elements: Self) -> None:
        for element in elements:
            element.parent = self.__class__
            self._childs.append(element)
    
    def _wrap_with_string(self, text: str) -> str:
        return f'"{text}"'

    def __str__(self):
        return f"<{self.elementType}{' class = ' + self._wrap_with_string(self.className) if self.className else ''}{' id = ' + self._wrap_with_string(self.id) if self.id else ''}>{self.innerHTML if self.innerHTML else ''}</{self.elementType}>"
