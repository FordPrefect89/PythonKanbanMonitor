import Tkinter as tk

class ExampleApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,
                          master,
                          width=300,
                          height=200)
        self.master.title('Kanban Monitor')
        self.pack_propagate(0)
        self.pack()
        
        self.FrameLbl = tk.LabelFrame(self, text='Kanban Location')
        self.kanban_var = tk.StringVar()
        self.kanban = tk.OptionMenu(self,
                                    self.kanban_var,
                                    ' ',
                                    'Combiner',
                                    'Computer',
                                    'OHU')
        self.kanban_var.set('        ')
        self.btnSubmit = tk.Button(self,
                                   text='Start Monitor',
                                   command=self.StartMonitor)
        self.btnSubmit.pack(side=tk.BOTTOM)
        self.kanban.pack(side=tk.LEFT)

    def StartMonitor(self):
            print('%s monitoring started' % (self.kanban_var.get()))

    def run(self):
            self.mainloop()

app = ExampleApp(tk.Tk())
app.run()
