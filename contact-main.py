'''
This is a fake main that allows for testing of the widgets.
'''
import tkinter as tk
import tkinter.ttk as ttk
#from form_widgets import *
from contact_form import ContactForm
#from text_dialog import TextDialog

class Eclass:
    pass

class Main(object):

    def __init__(self, cls):
        self.master = tk.Tk()
        self.master.wm_title('Testing')
        self.master.geometry('950x680')
        cls(self.master)
        #cls(self.master, 'Contact', 'notes', 1)

    def run(self):
        self.master.mainloop()

if __name__ == '__main__':

    main = Main(ContactForm)
    #main = Main(TextDialog)
    main.run()