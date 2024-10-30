# Let's explore some Python tools with a few examples

# ⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣶⣶⣶⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢀⣾⠟⠛⢿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢸⣿⣄⣀⣼⣿⣿⣿⣿⣿⣿⣿⠀⢀⣀⣀⣀⡀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣦⠀
# ⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⡇
# ⢰⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠋⠀⣼⣿⣿⣿⣿⣿⡇
# ⢸⣿⣿⣿⣿⣿⡿⠉⢀⣠⣤⣤⣤⣤⣤⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⡇
# ⢸⣿⣿⣿⣿⣿⡇⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀
# ⠘⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠁⠀⠀
# ⠀⠈⠛⠻⠿⠿⠇⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⡇⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣿⠇⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋

# ~(^-^)~



#################
# PRINTING TEXT #
#################

# # write "print()" and put the data you want to print in the parentheses "()"
# # it can be plain text
# print("HIYA")
# # it can be a variable
# hamburger = 27
# print(hamburger)
# # or it can be an expression
# print(10 * hamburger)



#######################
# DECLARING VARIABLES #
#######################

# # the syntax is always {name} = {value}
# var1 = 5
# var2 = 10
# print(var1 + var2)

# # you can re-declare variables to change their values
# var1 = 10
# var2 = 100
# print(var1 + var2)

# # there are a few different types of variables in Python, such as:
# intvar = 5 # int
# floatvar = 5.5 # float
# strvar = "hello" # string
# listvar = [1, 2, 3] # list
# dictvar = {"key": "value"} # dictionary

# # variables of different types don't interact nicely :(
# # (your coding environment will probably alert you to the errors in the following lines once they are uncommented)
# print(intvar + strvar) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(intvar + listvar) # TypeError: unsupported operand type(s) for +: 'int' and 'list'

# # but you can convert a variable's type, if it makes sense, to allow them to interact
# strvar = "5"
# strvar_as_int = int(strvar)
# print(intvar + strvar_as_int)



################################
# ACCESSING ELEMENTS IN A LIST #
################################

# # lists let you store multiple values at once
# mylist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# # and you can access any item (or "element") in the list by using its index
# print(mylist[1])
# print(mylist[2])

# # keep in mind that Python and most other languages start counting at 0
# # so the indices of the mylist are actually
# # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# # NOT
# # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# print(mylist[10]) # IndexError: list index out of range

# # you can also use negative indices to go backwards from the end of the list
# print(mylist[-1])
# print(mylist[-9])

# # or you can take a "slice" of the list to get a range of elements from within
# print(mylist[0:4]) # the first 4 elements (up to but not including index 4)

# # this works with negative indices too
# print(mylist[-5:-1])

# # there are a few more neat but less important things you can do with list indexing
# # print the whole list backwards:
# print(mylist[::-1]) # -1 is a "step" parameter: tells tells Python to count indices by -1
# # print a slice of the list backwards:
# print(mylist[-1:-5:-1])
# # print every other element:
# print(mylist[::2])
# # print every third element:
# print(mylist[::3])

# # if you're ever unsure of how to access elements in a list the way you want to, or how to code ANYTHING, Google is your friend!
# # There is almost always an explanation because someone has wondered the same thing as you.

# # For example, googling "python list backwards" directs you to https://stackoverflow.com/questions/3940128/how-do-i-reverse-a-list-or-loop-over-it-backwards
# # which provides several great answers. In general, StackOverflow.com is a fantastic resource for coding-related questions.



#########
# LOOPS #
#########

# # loops are where code starts to become really powerful.

# # Let's say you have a giant wall of text with one character unlike the rest:
# haystack = """
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOO0OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# """

# # If you want to find the unusual character, you could search manually by reading the text yourself one character at a time...
# # ...but that would take a long time and be boring :(

# # Let's just have Python do it for us!

# needle = "0" # this is what we're searching for...

# # To begin a loop, you start with the "for" keyword, then provide the variable you want to loop over, then a colon (":")
# # You also define a variable name ("piece_of_hay" in this case) to represent each element in the list
# for piece_of_hay in haystack:
    

#     # now you indent (press "Tab")
#     # and provide the code you want to run for each element in the list
#     if piece_of_hay == needle:
#         print("Found the needle!")

#         # Here we "break" out of the loop because we got what we wanted and don't need to keep going
#         break
#     else:
#         print("Not here.")

# # # What if you wanted to get the index of the character that contains the needle?
# # # We could modify the loop slightly to achieve that:
# # for i in range(len(haystack)): # "i" here is the index of each element. We could use any name but "i" is most often what you'll see.
# #     if haystack[i] == needle:
# #         print("Found the needle at index", i)
# #         break
# #     else:
# #         print("Not here.")



###############################
# CHALLENGE 1: 5-letter Names #
###############################

# # Say you have a list of names:
# names = [
#     "Bob",
#     "Bobby",
#     "Sal",
#     "Sally",
#     "Bernard",
#     "Marissa",
#     "Sam",
#     "Samantha",
#     "Nancy",
#     "Thomas"
# ]

# # Print all the names with exactly 5 characters



##############################
# CHALLENGE 2: COUNTING BY 5 #
##############################

# Write a loop to print every fifth number between 1 and 1000
# (5, 10, 15, ..., 1000)

# Hint: you may need to declare a variable before starting the loop
    


#########################
# CHALLENGE 3: FizzBuzz #
#########################

# For every number between 1 and 100, print "Fizz" if the number is divisible by 3,
# "Buzz" if the number is divisible by 5, and "FizzBuzz" if the number is divisible by both 3 and 5.



# Alright, that's it for it for today!

# With this knowledge of variables, lists, loops, and printing text, we can already do a lot with Python. You'll find as we go deeper that these tools show up
# again and again, even in more complex programs like video games.

# With just a few more tools in our kit, we'll be ready to start building some awesome projects!



##################
# Moving Forward #
##################

# If you ever get stuck, I recommend using Google and searching for StackOverflow answers first.
# If that doesn't answers your question, try asking Claude (claude.ai) or ChatGPT (chatgpt.com) for help.
# They _can_ be wrong, so test the code yourself! But generally they give great advice.
# Claude tends to be more reliable, in my experience, but feel free to experiment and see which you prefer.