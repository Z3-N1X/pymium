from core import Space

def getElementById(space: Space, id: str) -> list:
    results = list()

    return _find_in_list_by_id(space.elements, id)

def _find_in_list_by_id(choosen_list: list, id: str) -> list:
    results = list()

    for element in choosen_list:
        if type(element) == list:
            results = results + _find_in_list_by_id(element, id)
            continue

        if element.id == id:
            results.append(element)
    return results

