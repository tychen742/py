### import module
import hello as h

### call function and get a RETURN
greeting_returned = h.hello("T.Y.")
print("fuction return: ", greeting_returned)

### call variable
print("The sky in hell.py is: ", h.sky_color)

### call class
greeting = h.Person("T.Y.", 35)
greeting.greet()
