import tkinter as tk
from tkinter import ttk #has adv widgets
from tkinter import scrolledtext
from tkinter import Menu

#create instance
win = tk.Tk()

#add a title
win.title("Python GUI")

#creating a container frame to hold all other widgets
monty = ttk.LabelFrame(win, text=' Monty Python')
monty.grid(column=0, row=0)

#grid manager, modify adding a Label
#aLabel = ttk.Label(monty, text=" ")
#aLabel.grid(column=0, row=0)

#Button Click Event Function
def clickMe():
    action.configure(text='Hello ' + name.get() + ' ' + numberChosen.get())

#changing our label
ttk.Label(monty, text="Enter a name:").grid(column=0, row =0, sticky='W')

#ttk is not a python
#adding a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky=tk.W)

#adding a button
action = ttk.Button(monty, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)
#action.configure(state='disabled')#disable the button widget

ttk.Label(monty, text="Choose a number:").grid(column=1, row =0)
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number)
numberChosen['values'] = (1,2,4,42,100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

#creating 3 checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty, text="Disabled", variable=chVarDis, state = 'disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(monty, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W) #W means aligned to the west/left

#using a scrolled text control
scrolW = 30
scrolH = 3 #these values are magic numbers found by experimentation to work well
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)
#columnspan makes the widget spread to three columns
#tk.Word - telling the scroll widget to break lines by word

#change radiobutton global variables into a list
colors = ["Blue", "Gold", "Red"]

#Radiobutton Callback
def radCall():
    radSel=radVar.get()
    if radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])
    elif radSel == 3: win.configure(background=colors[3])

#create three Radio buttons using one varialbe
#setting the default value outside the range of the radiobutton widgets inorder to trigger the callbacks
radVar = tk.IntVar()

#Changed the callback function to be 0 based indexing, using the list instead of module-level global variables
#Next we are selecting a non-existing index value for radVar
radVar.set(99)

#Now we are creating all three Radio button widgets within one loop
for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W, columnspan=3)

#create a container to hold labels
labelsFrame = ttk.LabelFrame(monty, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7, padx=20, pady=40)

#place labels into the container element, ttk = theme tk
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1, sticky=tk.W)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2, sticky=tk.W)

#grid_configure allow to modify the spaces in between the frame
#winfo_children returns a list of children belonging to the frame variable
for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=1)

#Exit GUI cleanly
#_ means a private function not to be called by clients of our code
def _quit():
    win.quit()
    win.destroy()
    exit()

#creating a Menu Bar
menuBar = Menu(win)
win.config(menu=menuBar)

#add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", comman=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

#add another menu to the menu bar
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

#place cursor into the Entry
nameEntered.focus() 

win.mainloop()
