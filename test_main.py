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
        super().__init__(owner, 'Contact', columns=4)

        self.width1 = 50
        self.width2 = 20
        self.add_title('Contacts')
        self.add_label('Name:')
        self.add_entry('name', 3, str, width=self.width1)
        #self.add_spacer(1)

        self.add_label('Address1:')
        self.add_entry('address1', 3, str, width=self.width1)
        #self.add_spacer(1)

        self.add_label('Address2:')
        self.add_entry('address2', 3, str, width=self.width1)
        #self.add_spacer(1)

        self.add_label('City:')
        self.add_entry('city', 1, str, width=self.width2)
        #self.add_spacer(1)

        self.add_label('State:')
        self.add_entry('state', 1, str, width=self.width2)
        #self.add_spacer(1)

        self.add_label('Post Code:')
        self.add_entry('zip', 1, str, width=self.width2)

        self.add_label('Country:')
        self.add_entry('country', 1, str, width=self.width2)

        self.add_label('Email:')
        self.add_entry('email_address', 1, str, width=self.width2)
        self.add_spacer(1)
        self.add_spacer(1)

        self.add_label('Phone:')
        self.add_entry('phone_number', 1, str, width=self.width2)
        self.add_spacer(1)
        self.add_spacer(1)

        self.add_label('Web Site:')
        self.add_entry('web_site', 3, str, width=self.width1)

        self.add_label('Description:')
        self.add_text('description', 3, width=self.width1+4, height=20)

        self.add_ctl_button('Next')
        self.add_ctl_button('Prev')
        self.add_btn_spacer()
        self.add_ctl_button('Save')
        self.add_ctl_button('Edit', class_name=Eclass)
        self.load_form()

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