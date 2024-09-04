
class Style:
    def __init__(self, **styles) -> None:
        self.styles = styles
        
    def __str__(self) -> str:
        results = ""
        for key in self.styles.keys():
            results += key + ":" + self.styles[key] + ";"
        return results
    