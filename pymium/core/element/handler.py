from pymium.core import Space
from pymium.core.element import Element
def getElementById(space: Space, id: str) -> list[Element]:
    return _find_in_list_by_id(space.elements, id)

def _find_in_list_by_id(choosen_list: list, id: str) -> list:
    results = list()

    for element in choosen_list:

        if element.childs:

            results = results + _find_in_list_by_id(element.childs, id)

        if element.id == id:
            results.append(element)
    return results

