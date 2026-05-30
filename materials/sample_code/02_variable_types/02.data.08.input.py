input_something = input("Please enter your name:")

print("Your name is:", input_something)

### time converter ###
str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)  # convert string to integer

hours = total_secs // 3600  # use integer divisor
secs_still_remaining = total_secs % 3600  # use modulus divisor
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)  # use comma to separate entries
