from pymium import * 

body_style = Style(display= "flex", justify_content="center")

base_style= body_style.clone()
base_style.add_style(color="black", flex_direction="column")
button_style = base_style.clone()

button_style.add_style(background = "blue")

container = Element(Types.div, "main-container", style=base_style)
heading = Element(Types.h1, "a-heading", innerHTML="Hello", style=Style(text_align="center"))
def e():
    print("bobux")
abutton = Element(Types.button, "a-button", 'button-class', 'you wassup', onclick=e)

space = Space("Main")
space.append(container)
container.append(heading, abutton)

element_with_main_container_id = handler.getElementById(space, "main-container")[0]
element_with_main_container_id.style.add_style(background_color = "gray", border_radius="10px")

run(space)
print("e")