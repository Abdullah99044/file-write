import tkinter as tk
from tkinter.constants import TRUE, X, Y
window = tk.Tk()

#button = tk.Button(text='...', bg="white", fg="black")
#button.pack(pady = 20, padx = 20 )

# schijf hier tussen je code

def log_function(x):

    file = open("actions1.gitignore" , 'a') 
    if x == 1:
        file.write("Licht is oof!\n")
    else:
        file.write("Licht is on!\n")
    file.close()


x = TRUE
 
def licht_functie_on():
    global window
    global x
    global y
    global button
    
    if x:
        log_function(0)
        window.config(bg="yellow")
        button.config(text="Switch light on")
        x = False
    else:
        log_function(1)
        window.config(bg="black")
        button.config(text="Switch light off")
        x = True
    

 
 

 
 

 
window.config(bg="black")
button = tk.Button(window , text="Switch light on" , bg="white"   , command=licht_functie_on )
 
button.pack(pady = 20, padx = 20 )


# schijf hier tussen je code

window.mainloop()
