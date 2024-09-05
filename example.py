from pymium import * 

base_style= Style(color="red")
button_style = base_style.clone()
button_style.add_style(background = "blue")

container = Element(Types.div, "main-container")
heading = Element(Types.h1, "a-heading", innerHTML="Hello", style=base_style)
abutton = Element(Types.button, "a-button", 'button-class', 'you wassup')

space = Space("Main")
space.append(container)
container.append(heading, abutton)

element_with_main_container_id = handler.getElementById(space, "main-container")[0]
element_with_main_container_id.style.add_style(background_color = "green", border_radius="10px")

run(space)
