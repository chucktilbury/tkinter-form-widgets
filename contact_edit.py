import tkinter as tk
from forms import Forms

class _contact_edit_form(Forms):

    def __init__(self, owner, row_index):
        '''
        This form allows editing the data.
        '''
        super().__init__(owner, 'Contact', columns=4)

        self.width1 = 70
        self.width2 = 30
        self.row_index = row_index

        self.add_title('Edit Contacts')

        self.add_label('Name:')
        dups = self.add_entry('name', 3, str, width=self.width1)
        self.add_dupe_check(dups)

        self.add_label('Address1:')
        self.add_entry('address1', 3, str, width=self.width1)

        self.add_label('Address2:')
        self.add_entry('address2', 3, str, width=self.width1)

        self.add_label('City:')
        self.add_entry('city', 1, str, width=self.width2)

        self.add_label('State:')
        self.add_entry('state', 1, str, width=self.width2)

        self.add_label('Post Code:')
        self.add_entry('zip', 1, str, width=self.width2)

        self.add_label('Country:')
        self.add_entry('country', 1, str, width=self.width2)

        self.add_label('Email:')
        self.add_entry('email_address', 1, str, width=self.width2)

        self.add_label('Phone:')
        self.add_entry('phone_number', 1, str, width=self.width2)

        self.add_label('Web Site:')
        self.add_entry('web_site', 3, str, width=self.width1)

        self.add_label('Description:')
        self.add_text('description', 3, width=self.width1+7, height=20)

    def add_new_buttons(self):
        self.add_ctl_button('Save')

    def add_edit_buttons(self):
        self.add_ctl_button('Next')
        self.add_ctl_button('Prev')
        self.add_btn_spacer()
        self.add_ctl_button('Save')

class ContactEdit(tk.Toplevel):

    def __init__(self, owner, row_id):
        super().__init__(owner)
        self.transient(owner)

        self.upper_frame = tk.Frame(self)
        self.upper_frame.grid(row=0, column=0)
        self.lower_frame = tk.LabelFrame(self)
        self.lower_frame.grid(row=1, column=0)

        self.cf = _contact_edit_form(self.upper_frame, row_id)
        self.cf.grid()
        self.cf.add_edit_buttons()
        tk.Button(self.lower_frame, text='Dismiss', command=self._dismiss_btn).grid()
        self.cf.load_form()
        self.wait_window(self)

    def _dismiss_btn(self):
        self.cf.check_save()
        self.destroy()

class NewContact(tk.Toplevel):

    def __init__(self, owner):
        super().__init__(owner)
        self.transient(owner)

        self.upper_frame = tk.Frame(self)
        self.upper_frame.grid(row=0, column=0)
        self.lower_frame = tk.LabelFrame(self)
        self.lower_frame.grid(row=1, column=0)

        self.cf = _contact_edit_form(self.upper_frame, 0)
        self.cf.grid()
        self.cf.new_flag = True
        self.cf.add_new_buttons()
        tk.Button(self.lower_frame, text='Dismiss', command=self._dismiss_btn).grid()
        self.wait_window(self)

    def _dismiss_btn(self):
        self.cf.check_save()
        self.destroy()
