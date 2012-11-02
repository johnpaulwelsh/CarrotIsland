#!/usr/bin/python
from Tkinter import *

def create_main():
    # Creates title
    frame1 = Frame(top, relief=GROOVE, borderwidth=2)
    label1 = Label(frame1, text='Thomas Edison: Paranormal Inquisitor', font=('Arial', 48), fg="blue")
    label1.pack(side="left")
    
    # Creates window
    top.create_window(540, 300, window=frame1, anchor=SE)
    top.pack(fill="both", expand="yes")
    
    # Creates start button
    frame2 = Frame(top, relief=GROOVE, borderwidth=2)
    button1 = Button(frame2, text='Start', command=go_game, font=('Arial', 28), fg="blue")
    button1.pack(side="left")
    
    top.create_window(457, 450, window=frame2, anchor=SE)
    top.pack(fill='both', expand='yes')
    
    # Creates option button
    frame3 = Frame(top, relief=GROOVE, borderwidth=2)
    button2 = Button(frame3, text='Options', command=go_options, font=('Arial', 28), fg="blue")
    button2.pack(side="left")
    
    top.create_window(480, 550, window=frame3, anchor=SE)
    top.pack(fill='both', expand='yes')
    
    #Creates exit button
    frame5 = Frame(top, relief=GROOVE, borderwidth=2)
    button4 = Button(frame5, text='Quit',command=quit, font=('Arial', 28), fg="blue")
    button4.pack(side="left")
    
    top.create_window(455, 750, window=frame5, anchor=SE)
    top.pack(fill='both', expand='yes')
    
    return top

root = Tk()
root.title("Thomas Edison")
top = Canvas(root,width="800", height="800")
size = 100
cols = 8
rows = 8
squareList = []
for i in range(cols):
    for j in range(rows):
        if j%2: colours = ["black", "white"]
        else: colours = ["white", "black"]
        squareList.append(top.create_rectangle(i*size,  j*size,
                                               i*size+size, j*size+size,
                                               fill=colours[i%2]))
currentframe = mainframe = create_main()
helpframe = creat_help()
optionsframe = create_options()
gameframe = create_game()

go_main()

root.mainloop()