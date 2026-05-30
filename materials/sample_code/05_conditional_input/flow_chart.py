import schemdraw
from schemdraw.flow import *

with schemdraw.Drawing() as d:
    d+= Start().label("Start")
    d+= Arrow().down(d.unit/2)
    
    #Input the string 
    d+= Data(w = 4).label("User input string:\n string_a")
    d+= Arrow().down(d.unit/2)
    
    #Reverse the string
    d+= Box(w = 4).label("Reverse the string:\n string_a_reversed")
    d+= Arrow().down(d.unit/2)
    
    #Check if string and reverse_string are same
    d+= (decision := Decision(w = 5, h= 5,
                       S = "True",
                        E = "False").label("CONDITION: \n string_a\n == \nstring_a_reversed?"))
    
    #If True
    d+= Arrow().length(d.unit/2)
    d+= (true := Box(w = 5).label("Print statement:\n string_a is a palindrome."))
    d+= Arrow().length(d.unit/2)
    
    #End program
    d+= (end := Ellipse().label("End"))
    
    #If False. Start the arrow from East of decision box
    d+= Arrow().right(d.unit).at(decision.E)
    
    #false is referring to the box where string is not a palindrome.
    d+= (false := Box(w = 5).label("Print statement:\n string_a is not\n a palindrome."))
    
    #Add a downward arrow from the South of false box 
    d+= Arrow().down(d.unit*2.5).at(false.S)
    
    #Extend the arrow to reach the end of the program
    d+= Arrow().left(d.unit*2.15)
    d.save("output/palindrome_flowchart.svg", dpi = 300)