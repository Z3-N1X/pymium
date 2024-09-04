from pymium import * 
from core.base.style import Style


aDiv = Element(Types.div, "E")
nDiv = Element(Types.h1, "N", innerHTML="Hello")
space = Space("Main")
space.append(aDiv)
aDiv.append(nDiv)
print(str(Style(background_color= "red", color= "green")))

run(space)
