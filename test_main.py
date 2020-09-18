'''
This is a fake main that allows for testing of the widgets.
'''
import tkinter as tk
import tkinter.ttk as ttk
#from form_widgets import *
from forms import Forms

class Eclass:
    pass

class TestForm(Forms):

    def __init__(self, owner):
        '''
        Create some widgets.
        '''
        super().__init__(owner, 'table', columns=4)
        self.add_title('Test Title')
        self.add_label('test')
        self.add_entry('col', 3, str, width=51)
        #self.add_spacer(1)
        #self.add_spacer(1)

        self.add_label('test two')
        self.add_entry('col', 1, str)
        #self.add_spacer(1)

        self.add_label('test three')
        self.add_entry('col', 1, str)
        #self.add_spacer(1)

        self.add_ctl_button('Next')
        self.add_ctl_button('Prev')
        self.add_btn_spacer()
        self.add_ctl_button('Save')
        self.add_ctl_button('Edit', class_name=Eclass)

class Main(object):

    def __init__(self, cls):
        self.master = tk.Tk()
        self.master.wm_title('Testing')
        #self.master.geometry('950x500')
        cls(self.master)

    def run(self):
        self.master.mainloop()

if __name__ == '__main__':

    main = Main(TestForm)
    main.run()