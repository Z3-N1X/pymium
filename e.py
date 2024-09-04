from pymium import * 


aDiv = Element(Types.div, "E")
nDiv = Element(Types.h1, "N", innerHTML="Hello")
space = Space("Main")
space.append(aDiv)
aDiv.append(nDiv)

run(space)
