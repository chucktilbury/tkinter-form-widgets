'''
This is the main implementation file for the form widgets. These widgest are designed
to give clean and automated access to a database. The Database class is assumed to
already have the database open and ready to use.

These widgets are intended to be used with the forms module that is included in this
source code.
'''
import tkinter as tk
import tkinter.ttk as ttk
from database import Database

class _form_widget_base(tk.Frame):
    '''
    This class implements the basic functions for all of the form widgets and
    invokes the database.
    '''

    def __init__(self, owner, table, column):
        super().__init__(owner)
        self.data = Database.get_instance()
        self.owner = owner
        self.table = table
        self.column = column
        self.row_id = None

    def getter(self):
        '''
        Stub function. The getter reads the widget and saves the data into the database as
        a single row/column entry.
        '''

    def setter(self):
        '''
        Stub function. The setter reads the database as a single row/column entry and saves
        it into the widget.
        '''

    def clear(self):
        '''
        Clears the widget.
        '''

    def populate(self):
        '''
        For compound widgets, this can grab a list from the database and place it into the
        widget. For other widgets, it simply does the same as a setter().
        '''
        self.setter()

    def set_row_id(self, row_id):
        '''
        This must be called before the value of the widget can be read or written.
        '''
        self.row_id = row_id

class formEntry(_form_widget_base):
    '''
    Wrapper for the tkinter Entry widget.
    '''

    def __init__(self, owner, table, column, _type, **kw):
        super().__init__(owner, table, column)
        self._type = _type

        self.value = tk.StringVar(self)
        self.widget = tk.Entry(self, textvariable=self.value, **kw)
        self.widget.grid()

    def getter(self):
        val = self._type(self.value.get())
        self.data.write_single_value(self.table, self.column, self.row_id, val)

    def setter(self):
        state = self.widget.configure()['state']
        if state == 'readonly':
            self.widget.configure(state='normal')

        val = self.data.read_single_value(self.table, self.column, self.row_id)
        self.value.set(str(val))

        if state == 'readonly':
            self.widget.configure(state='readonly')

    def clear(self):
        state = self.widget.configure()['state']
        if state == 'readonly':
            self.widget.configure(state='normal')

        self.value.set('')

        if state == 'readonly':
            self.widget.configure(state='readonly')

class formText(_form_widget_base):

    def __init__(self, owner, table, column, **kw):
        super().__init__(owner, table, column)

        self.local_frame = tk.Frame(self, bd=1, relief=tk.RIDGE)
        self.widget = tk.Text(self.local_frame, wrap=tk.NONE, **kw)
        self.widget.insert(tk.END, '')
        self.widget.grid(row=0, column=0, sticky='nw')

        self.vsb = tk.Scrollbar(self.local_frame, orient=tk.VERTICAL)
        self.vsb.config(command=self.widget.yview)
        self.widget.config(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=0, column=1, sticky='nse')

        self.hsb = tk.Scrollbar(self.local_frame, orient=tk.HORIZONTAL)
        self.hsb.config(command=self.widget.xview)
        self.widget.config(xscrollcommand=self.hsb.set)
        self.hsb.grid(row=1, column=0, sticky='wes')

        self.local_frame.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')

    def getter(self):
        value = self.widget.get(1.0, tk.END)
        self.data.write_single_value(self.table, self.column, self.row_id, value)

    def setter(self):
        value = self.data.read_single_value(self.table, self.column, self.row_id)
        self.widget.delete('1.0', tk.END)
        if not value is None:
            self.widget.insert(tk.END, str(value))

    def clear(self):
        self.widget.delete('1.0', tk.END)

class formCombobox(_form_widget_base):

    def __init__(self, owner, val_tab, val_col, pop_tab, pop_col, **kw):
        super().__init__(owner, val_tab, val_col)

        self.pop_tab = pop_tab
        self.pop_col = pop_col

        self.widget = ttk.Combobox(self, state='readonly', **kw)
        self.populate()
        self.widget.grid()

    def getter(self):
        value = self.widget.current()+1
        self.data.write_single_value(self.table, self.column, self.row_id, value)

    def setter(self):
        self.populate()
        value = self.data.read_single_value(self.table, self.column, self.row_id)
        self.widget.current(int(value)-1)

    def clear(self):
        try:
            self.widget.current(0)
        except tk.TclError:
            pass # empty content is not an error

    def populate(self):
        self.widget['values'] = self.data.get_column_list(self.pop_tab, self.pop_col)

class formDynamicLabel(_form_widget_base):

    def __init__(self, owner, table, column, **kw):
        super().__init__(owner, table, column)

        self.value = tk.StringVar(self)
        self.widget = tk.Label(self, textvariable=self.value, **kw)
        self.widget.grid()

    def setter(self):
        value = self.data.read_single_value(self.table, self.column, self.row_id)
        self.value.set(str(value))

class formIndirectLabel(_form_widget_base):

    def __init__(self, owner, val_tab, val_col, rem_tab, rem_col, **kw):
        super().__init__(owner, val_tab, val_col)

        self.rem_tab = rem_tab
        self.rem_col = rem_col

        self.value = tk.StringVar(self)
        self.widget = tk.Label(self, textvariable=self.value, **kw)
        self.widget.grid()

    def getter(self):
        # This is the name
        value = self.value.get()
        # find the row ID where the name matches in the rem_tab
        id = self.data.get_row_id(self.rem_tab, self.rem_col, value)
        # set the value with the row_id
        self.data.write_single_value(self.table, self.column, self.row_id, id)

    def setter(self):
        # this is the ID
        id = self.data.read_single_value(self.table, self.column, self.row_id)
        # find the value with the row ID in the table
        value = self.data.read_single_value(self.rem_tab, self.rem_col, id)
        # set the widget value
        self.value.set(str(value))

    def clear(self):
        self.value.set('')

class formTitle(_form_widget_base):

    def __init__(self, owner, value, **kw):
        super().__init__(owner, None, None)

        self.widget = tk.Label(self, text=value, font=("Helvetica", 14), **kw)
        self.widget.grid()

class formCheckbox(_form_widget_base):

    def __init__(self, owner, table, column, **kw):
        super().__init_(owner, table, column)

        self.value = tk.IntVar()
        self.widget = tk.Checkbutton(self, variable=self.value, **kw)
        self.widget.grid()

    def getter(self):
        val = self.int(self.value.get())
        self.data.write_single_value(self.table, self.column, self.row_id, val)

    def setter(self):
        val = self.data.read_single_value(self.table, self.column, self.row_id)
        self.value.set(val)

    def clear(self):
        self.value.set(0)
