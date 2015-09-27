#!/usr/bin/python

import Tkinter

class simpleapp_tk(tkinter.Tk())
    def ___init___(self,parent)
        tkinter.Tk.___init___(self,parent)
        self.parent = parent
        self.initialize()

    def initalize(self)
        pass

if ___name___ == "___main___"
    app = simpleapp_tk(none)
    app.title('my application')
    app.mainloop()
