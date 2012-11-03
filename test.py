#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This program creates a quit
button. When we press the button,
the application terminates. 

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

from Tkinter import *
from ttk import *

class Window(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Thomas Edison : Paranormal Inquisitor")
        self.style = Style()
        self.style.theme_use("clam")

        self.pack(fill=BOTH, expand=1)
        """
        set
        x = 427.5 
        and 
        y = 270 + or - 45 
        (30 for size of button,
         15 for spacing)
        """
        playButton = Button(self, text="Play",
            command=self.quit)
        playButton.place(x=427.5, y=225)
        
        optionButton = Button(self, text="Options",
            command=self.optionUI)
        optionButton.place(x=427.5, y=270)
        
        quitButton = Button(self, text="Quit",
            command=self.quit)
        quitButton.place(x=427.5, y=315)
        """
        Option UI is going 
        to replace the
        main screen when
        anyone clicks on 
        the Option Button. 
        """
    def optionUI(self):
        
        self.parent.title("Thomas Edison : Paranormal Inquisitor")
        self.style = Style()
        self.style.theme_use("clam")
        
        self.pack(fill=BOTH, expand = 1)
        
        configButton = Button(self, text = "Back",
                              command=self.initUI)
        configButton.place(x=427.5, y=270)
        

def main():
  
    root = Tk()
    root.geometry("960x540+300+300")
    app = Window(root)
    root.mainloop()  


if __name__ == '__main__':
    main()
