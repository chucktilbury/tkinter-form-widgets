'''
This is a fake main that allows for testing of the widgets.
'''
import tkinter as tk
import tkinter.ttk as ttk
from form_widgets import *

class TestClass(object):

    def __init__(self, owner):
        '''
        Create some widgets.
        '''
        ent = formEntry(owner, 'table', 'col', str)
        ent.set_row_id(1)
        ent.grid()
        ent.getter()
        ent.setter()
        ent.populate()
        ent.clear()


class Main(object):

    def __init__(self, cls):
        self.master = tk.Tk()
        self.master.wm_title('Testing')
        self.master.geometry('950x500')
        cls(self.master)

    def run(self):
        self.master.mainloop()

if __name__ == '__main__':

    main = Main(TestClass)
    main.run()