from typing import Self


class Style:
    def __init__(self, **styles) -> None:
        self.styles = styles

    def add_style(self, **styles):
        self.styles = self.styles | styles

    def clone(self) -> Self:
        return Style(**self.styles)
        
    def __str__(self) -> None | str:
        if not self.styles:
            return None
        results = ""
        for key in self.styles.keys():
            results += key.replace("_","-") + ":" + self.styles[key] + ";"
        return results
    