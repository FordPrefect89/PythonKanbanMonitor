#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
from KanbanMonitor import *

root = Tk()
root.wm_title('Kanban Monitor')
app = MainKanbanForm(root)
root.mainloop()
