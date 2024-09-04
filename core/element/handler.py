from core import Space

def getElementById(space: Space, id: str) -> list:
    results = list()

    for element in space.elements:
        if element.id == id:
            results.append(element)

def find_in_list(choosen_list: list, id: str) -> list:
    results = list()

    for element in choosen_list:
        if type(element) == list:
            results = results + find_in_list(element, id)
            continue

        if element.id == id:
            results.append(element)


    return results

