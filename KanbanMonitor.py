#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *

class MainKanbanForm:
    def __init__(self, master):
        mainForm = Frame(master)
        mainForm.grid()

        defaultValue = StringVar(mainForm)
        btnStartText = StringVar(mainForm)
        btnStopText  = StringVar(mainForm)
        defaultValue.set(' ')
        btnStartText.set('Start Monitor')
        btnStopText.set('Stop Monitor')

        cmbKanbanLocation = OptionMenu(mainForm,
                                       defaultValue,
                                       'Combiner',
                                       'Computer',
                                       'OHU')
        cmbKanbanLocation.config(width=15, font = 'Helvetica 14')
        lblKanbanLocation = Label(mainForm,
                                  text='Select Kanban Location')
        lblKanbanLocation.config(font = 'Helvetica 14')

        btnStart = Button(mainForm,
                          textvariable = btnStartText,
                          bg='green',
                          fg='white',
                          command = lambda: StartMonitor())
        btnStart.config(font = 'Helvetica 14')

        btnStop = Button(mainForm,
                         textvariable = btnStopText,
                         bg = 'red',
                         fg = 'white',
                         command = lambda: StopMonitor())
        btnStop.config(font = 'Helvetica 14')

        lblSlot01 = Label(mainForm, text = 'Slot 1', bg = 'red', fg = 'white')
        lblSlot02 = Label(mainForm, text = 'Slot 2', bg = 'red', fg = 'white')
        lblSlot03 = Label(mainForm, text = 'Slot 3', bg = 'red', fg = 'white')
        lblSlot04 = Label(mainForm, text = 'Slot 4', bg = 'red', fg = 'white')
        lblSlot05 = Label(mainForm, text = 'Slot 5', bg = 'red', fg = 'white')
        lblSlot06 = Label(mainForm, text = 'Slot 6', bg = 'red', fg = 'white')
        lblSlot07 = Label(mainForm, text = 'Slot 7', bg = 'red', fg = 'white')
        lblSlot08 = Label(mainForm, text = 'Slot 8', bg = 'red', fg = 'white')

        lblSlot01.config(width=20, font = 'Helvetica 14')
        lblSlot02.config(width=20, font = 'Helvetica 14')
        lblSlot03.config(width=20, font = 'Helvetica 14')
        lblSlot04.config(width=20, font = 'Helvetica 14')
        lblSlot05.config(width=20, font = 'Helvetica 14')
        lblSlot06.config(width=20, font = 'Helvetica 14')
        lblSlot07.config(width=20, font = 'Helvetica 14')
        lblSlot08.config(width=20, font = 'Helvetica 14')

        lblKanbanLocation.grid(column = 0,
                               row = 1,
                               sticky = 'EW')
        cmbKanbanLocation.grid(column = 1,
                               row = 1)
        btnStart.grid(column = 0,
                      row = 2,
                      pady = 10)
        btnStop.grid(column = 1,
                     row = 2,
                     pady = 10)
        lblSlot01.grid(column = 0, row = 3, padx = 2, pady = 2)
        lblSlot02.grid(column = 0, row = 4, padx = 2, pady = 2)
        lblSlot03.grid(column = 0, row = 5, padx = 2, pady = 2)
        lblSlot04.grid(column = 0, row = 6, padx = 2, pady = 2)
        lblSlot05.grid(column = 1, row = 3, padx = 2, pady = 2)
        lblSlot06.grid(column = 1, row = 4, padx = 2, pady = 2)
        lblSlot07.grid(column = 1, row = 5, padx = 2, pady = 2)
        lblSlot08.grid(column = 1, row = 6, padx = 2, pady = 2)

        def StartMonitor():
            print('Monitoring started for', defaultValue.get())

        def StopMonitor():
            print('Monitoring Stopped for', defaultValue.get())
