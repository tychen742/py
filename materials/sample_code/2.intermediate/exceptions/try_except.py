# ##### try...except block  # ####
# ##### test for errors     # ####
try:                        # #### try block contains the test
    num > 3                 # #### num is not defined
                            # #### good for handling files because you don't knwo
                            # #### if the files will be there or not
except:                     # #### when error/exception, run except block
    print("Something is wrong")
else:                       # #### else (no error), run this
    print("Nothing is wrong")
finally:                    # #### always run the finally block
    print("The finally block is run")
