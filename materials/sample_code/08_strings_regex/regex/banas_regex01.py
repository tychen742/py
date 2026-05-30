### Banas Regex

########## Number, Space, and Character ##########


\d # any number
\d{1,5} #between 1 to 5 digits
\D # anything but a number

\w # any character
\w+ # a series of characters w: character; +: ONE OR MORE characters 
\W # anything but a char

\s # any space
\S # anything but a space
\b # space follow or proceed a whole word # "My Dog" --> the space between my and dog

. # anything but a line break
\. # any possible character; \: regex code 


'Jennifer\s\w+\s' # looking for last name

? # 0 or 1 repetition of the code proceeds it
* # 0 or more repetitions
{n} # expects n repetitions
{n} \d{5} # expect to find 5 digits in a row
{n} \{1,5} # expect to find BETWEEN 1 and 5 digits in a ROW

########## ESCAPING ##########
# escaping means something be followed by a back slash
# $ and . are to be escaped
### e.g., you need to search for dollar amount.
\$\d*\.\d{2} # $100.00
##### Other regex codes to be escaped IF you want to SEARCH FOR THEM
# $ == the end of a sentence
(
)
*
+
?
[
\
^
]
|
\e # escape white space to SEARCH for white space
\f # Form feed
\n # line feed; New line: moving one line forward
\r # Carriage return: move the cursor to the beginning of the line  
\t # tab 

##### How to search for wrongly spelled words #####
calend[ae]r # search for either calendar or caldender 
[a-z] # search any lower case letters
[0-9] # search for any number
[A-F] # search for any UPPER case letters
[A-Fa-t0-4] # search for upper case from A to F, lower case from a to t, and number from 0 to 4
