from pymium import * 
import os
space = Space("Main")
body_style = Style(display= "flex", justify_content="center")

base_style= body_style.clone()
base_style.add_style(color="black", flex_direction="column")
button_style = base_style.clone()

button_style.add_style(background = "blue")

container = Element(Types.div, "main-container", style=base_style)
heading = Element(Types.h1, "a-heading", innerHTML="Hello", style=Style(text_align="center"))
def e():
    print("clicked")
    style = Style(color="red !important")
    heading.innerHTML = "hi"
    heading.style = style
    win.set_html(space)

abutton = Element(Types.button, "a-button", 'button-class', 'you wassup', onclick=e)

space.append(container)
container.append(heading, abutton)

element_with_main_container_id = handler.getElementById(space, "main-container")[0]
element_with_main_container_id.style.add_style(background_color = "gray", border_radius="10px")
win = PyWindow(space)


win.run()
print("e")