
#%%
#This is a cell.  A cell is a block of code delineated by the #%% which defines the 
#start of a new cell. 
#
#All lines in a python program are either lines to be executed or comments. 
#
#Comment lines are indicated by a # symbol at the start of the line.   This is where 
#I will provide instruction or you can make notes to indicate what you are doing and 
#to help you keep track of your program.  
#
#The next cell can be executed in two ways.  First, notice above and to the right is 
#an arrow which is the "run" button.  This will run the entire file.  
#Below are the words "Run Cell"
#

#%%
variable_name = "my_variable"
print(variable_name)
#%%
#Notice on the right is a panel called the interactive python console.  
#The panel is a window in which you can run python code, and see the output, 
#Notice that the first line of code is copied over followed by a ...
#click on that It should expand and show you all the code that was run in a cell
#The block of code is labeled with a number.    
#The output is separated from the input, at the line with the ... 
#The output is the resut of the print statement I gave above.   
#Now try the next cell 
#%% 
a = 1
b = 2
c = a + b 
print(c)
#%%
#From the view menu, select Terminal.  
#A window should open below and you should see a tab labeled Jupyter:Variables. 
#you should see the variables a,b,c, and variable_name.  The type of variable 
#is indicated (a,b,c are integers (int), variable_name is a string, i.e., text)
# The value of the variable is the last column.  
#%%
#Notice in the interactive python window on the bottom right is a box with a
# triangle and the words, "Type code here and press shift-enter to run"
# type  d = c-a and then either click on the triangle, or press shift-enter
# The code should run, and the variable d should have been created.   
#Run the next cell 
#%%
a = 5 
b = 4

c = a*b  #multiply
#print(c)
#%%
#Notice two things.  
#First, no output was generated because a comment was put in 
#front of "print(c)" preventing it from executing. 
#Second, in the variable explorer notice the values of a,b,c have changed. 
#%% This is where you put the cellname. I call it divide
#In the next example I do a calculation but I do not set it equal to any variable.  
#Try running it. 
a = 5
b = 4
a/b 
#Notice the output a/b appwars in the interactive window, but if you look in the 
# VARIABLES pane there is no variable with that name.  That value is "lost"
