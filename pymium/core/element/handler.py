from pymium.core import Space
from pymium.core.element import Element
def getElementById(space: Space, id: str) -> list[Element]:
    print("s")

    return _find_in_list_by_id(space.elements, id)

def _find_in_list_by_id(choosen_list: list, id: str) -> list:
    results = list()

    for element in choosen_list:
        print(1)
        if element.childs:
            print(2)
            results = results + _find_in_list_by_id(element.childs, id)
            print(3)
            
        print(element.id)
        if element.id == id:
            results.append(element)
    return results

