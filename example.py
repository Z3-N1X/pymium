from pymium import * 

style= Style(color="red")

container = Element(Types.div, "main-container")
heading = Element(Types.h1, "a-heading", innerHTML="Hello", style=style)

space = Space("Main")
space.append(container)
container.append(heading)

run(space)
