#video tutorial: https://www.youtube.com/watch?v=NzSCNjn4_RI

#'as' is used to create an alias of the imported module
#Tkinter is the fastest & easiest way to make GUI applications, alhthough it
# is considered outdated

import tkinter as tk

calculation=""

#'pass' is used as a placeholder for future code
def add_to_calculation(symbol):
    #global variable so we can manipulate inside of function
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end") #delete content of text result field
    text_result.insert(1.0, calculation) #1.0 is index where we insert string
    
def evaluate_calculation():
    global calculation
    try:
        #eval() evalulates a string expression and returns its value
        result = str(eval(calculation))
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

#create object
root = tk.Tk()

root.geometry("300x275")

#add a text field for the results
text_result = tk.Text(root, height = 2, width = 16, font = ("Spectral", 24))
text_result.grid(columnspan=5) #the text field will go across all 5 columns


#Create our Buttons! number corresponds to number button is for e.g. btn_1 stands for 1
#lambda functions aka anonymous function - does function when called rather than immediately

#Button 1
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Spectral", 14))
btn_1.grid(row = 2, column=1)

#Button 1
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Spectral", 14))
btn_1.grid(row = 2, column=1)

#Button 2
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Spectral", 14))
btn_2.grid(row = 2, column=2)

#Button 3
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Spectral", 14))
btn_3.grid(row = 2, column=3)

#Button 4
btn_1 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Spectral", 14))
btn_1.grid(row = 3, column=1)

#Button 5
btn_1 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Spectral", 14))
btn_1.grid(row = 3, column=2)

#Button 6
btn_1 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Spectral", 14))
btn_1.grid(row = 3, column=3)

#Button 7
btn_1 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Spectral", 14))
btn_1.grid(row = 4, column=1)

#Button 8
btn_1 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Spectral", 14))
btn_1.grid(row = 4, column=2)

#Button 9
btn_1 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Spectral", 14))
btn_1.grid(row = 4, column=3)

#Button 0
btn_1 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Spectral", 14))
btn_1.grid(row = 5, column=2)

#Button Plus
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Spectral", 14))
btn_plus.grid(row = 2, column=4)

#Button Minus
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Spectral", 14))
btn_minus.grid(row = 3, column=4)

#Button Multiplication
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Spectral", 14))
btn_mul.grid(row = 4, column=4)

#Button Division
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Spectral", 14))
btn_div.grid(row = 5, column=4)

#Button Paranthese Open
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Spectral", 14))
btn_open.grid(row = 5, column=1)

#Button Paranthese Close
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Spectral", 14))
btn_close.grid(row = 5, column=3)

#Button Equals
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Spectral", 14))
btn_equals.grid(row = 6, column=3, columnspan=2 ) #to fill up the space

#Button Clear
btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Spectral", 14))
#no lambda - no parameters; no parantheses - passing a function NOT calling it
#parameters need lambda expression
btn_clear.grid(row = 6, column=1, columnspan=2 ) #to fill up the space

root.mainloop()


#Errors: didn't adjust btn variable names (btn_1, btn_clear)
#wrote string instead of str

#troubleshooting: use print statements
# go through code in its entirety
#look at the moment the error occurs i.e. after the equals button, nothing pops up
#what the error was - I made the calculation variable empty before updating the display
