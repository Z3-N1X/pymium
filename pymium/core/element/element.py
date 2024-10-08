from pymium.core.base.types import ElementType
from pymium.core.base.style import Style
from typing import Optional, Self

class Element:
    def __init__(self,
                 elementType: ElementType,
                 id: Optional[str] = None,
                 className: Optional[str] = None,
                 innerHTML: Optional[str] = None,
                 style: Optional[Style] = None,
                 onclick  = None
                 ):
        self.elementType = elementType
        self.id = id
        self.className = className
        self.innerHTML = innerHTML
        self.style = style or Style()
        self._parent: Optional[Self] = None
        self._childs: list[Self] = []
        self.onclick = onclick
        self._att = dict()

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
    
    def _wrap_with_single_string(self, text: str) -> str:
        return f"'{text}'"

    def add_attributes(self, **attributes):
        self._att = attributes | self._att
    
    def customid(self) -> str:
        idName = self.id or "noId"
        className = self.className or "noClass"
        elementType = self.elementType
        return f"{elementType}:{idName}:{className}"

    def __str__(self):
        return f"<{self.elementType}{' class = ' + self._wrap_with_string(self.className) if self.className else ''}{' id = ' + self._wrap_with_string(self.id) if self.id else ''}{' onclick = ' + self._wrap_with_string('sendtopy('+self._wrap_with_single_string(self.customid())+')') if self.onclick else ''}{' style = ' + self._wrap_with_string(str(self.style)) if str(self.style) else ''}{''.join([' ' + att + '=' + self._wrap_with_single_string(self._att[att]) for att in self._att.keys()])}>{self.innerHTML if self.innerHTML else ''}{''.join([str(element) for element in self._childs])}</{self.elementType}>"
