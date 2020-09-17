'''
This module implements simple forms for the fom widgets. A form is generally intended
to be associated with a table in a database. The forms are fairly generic and should
be usable with any tkingter frame that might contain them. The forms are implemented
as a single compound widget.

A form consists of 2 frames. The left frame contains buttons that perform actions on
the fields of the form, such as saving it. The buttons are handled in this class. The
right frame contains the form widgets.

The form widgets are divided into columns so they can be layed out in a eye-pleasing
manner. The size of the widget and the column(s) in which it is placed is calculated
automatically.

All widgets have an optional label. If the lable is None, then the widget will be sized
to take up the entire column. Otherwise, the label will be considered a part of the
column.
'''

from database import Database
from form_widgets import *

class Forms(tkFrame):

    def __init__(self, owner, table, columns=2, form_width=500, **kw):
        super().__init__(owner, **kw)

        self.table = table
        self.data = Database.get_instance()

        # internal frames
        self.btn_frame = tk.Frame(self)
        self.btn_frame.grid(row=0, column=0, sticky='se')
        self.ctl_frame = tk.LabelFrame(self)
        self.ctl_frame.grid(row=0, column=1, sticky='nw')

        # widget layout information
        self.form_width = form_width    # Form width in pixels
        self.columns = columns          # Number of columns that the form will have
        self.row = 0        # The current row that is being layed out
        self.col = 0        # The current column
        self.ctl_xpad = 5   # horizontal padding for widgets
        self.ctl_ypad = 5   # horizontal padding for widgets

        # button layout information
        self.btn_row = 0    # current row to layout buttons on
        self.btn_xpad = 5   # horizontal padding for buttons
        self.btn_ypad = 5   # verticle padding for buttons
        self.btn_width = 10 # width of all buttons

        # row list management
        if table is None:
            self.row_list = None # getting the row list might be deferred
        else:
            self.row_list = self.data.get_id_list(self.table)
        self.row_index = 0

        # controls management
        self.ctl_list = []
        self.grid()


    # Methods that add control widgets to the form
    def add_label(self, text, **kw):
        '''
        Add a dead label to the form. This could be considered part of a control,
        but they are optionally added separately to facilitate lining them up.
        '''
        pass

    def add_title(self, text, **kw):
        '''
        A title spans all columns of the form and usually goes at the top or bottom
        of the form.
        '''
        pass

    def add_entry(self, column, cols, _type, **kw):
        '''
        This is the formEntry control.
        '''
        pass

    def add_text(self, column, cols, **kw):
        '''
        This is the formText control.
        '''
        pass

    def add_combo(self, column, cols, pop_tab, pop_col, **kw):
        '''
        This is the formCombobox control.
        '''
        pass

    def add_dynamic_label(self, column, cols, **kw):
        '''
        This is the formDynamicLabel control.
        '''
        pass

    def add_indirect_label(self, column, cols, rem_tab, rem_col, **kw):
        '''
        This is the formIndirectLabel control.
        '''
        pass

    def add_checkbox(self, column, cols, **kw):
        '''
        This is the formCheckbox control.
        '''
        pass

    def add_custom_widget(self, cls, **kw):
        '''
        This is any widget that has a self-contained class.
        '''
        pass

    def add_spacer(self, cols):
        '''
        This is an empty tk.Frame to simply take up spade.
        '''
        pass


    # Methods that add button widgets to the form
    def add_ctl_button(self, title, **kw):
        '''
        This adds a known control button to the form.
        '''
        pass

    def add_custom_button(self, cls, **kw):
        '''
        This adds a custom button from a self-contained class.
        '''
        pass

    def add_btn_spacer(self):
        '''
        Adds a space between buttons.
        '''
        pass


    # Methods that control the form
    def load_form(self):
        '''
        Call all of the setter functions for all of the widgets.
        '''
        pass

    def save_form(self):
        '''
        Call all of the getter functions for all of the widgets.
        '''
        pass

    # Standard button callbacks
    def _next_btn(self):
        '''
        Get the next row in the table and load the form.
        '''
        pass

    def _prev_btn(self):
        '''
        Get the previous row in the database and load the form.
        '''
        pass

    def _select_btn(self):
        '''
        Open the select dialog and select from the column in the row.
        '''
        pass

    def _new_btn(self):
        '''
        Clear the form or open the edit dialog.
        '''
        pass

    def _save_btn(self):
        '''
        Call all of the getter functions for all of the controls and
        commit the database changes.
        '''
        pass

    def _delete_btn(self):
        '''
        Delete the current row from the database and load the next one.
        '''
        pass

    def _edit_btn(self):
        '''
        Call up the edit dialog for this table row.
        '''
        pass


    # Other private functions
    def _get_geometry(self, wid):
        # Note that this does not work on frames or empty widgets.
        wid.update()
        return {'width':wid.winfo_width(), 'height':wid.winfo_height(),
                'hoffset':wid.winfo_x(), 'voffset':wid.winfo_y(),
                'name':wid.winfo_name()}

    def _grid(self, ctrl, cols):
        '''
        This calls the grid function on the control and sets it in the proper
        location with the proper size.
        '''
        if cols == self.columns:
            ctrl.grid(row=self.row, column=self.col, columnspan=self.columns)
            self.row += 1
            self.col = 0
        else:
            if self.col >= self.columns-1:
                ctrl.grid(row=self.row, column=self.col, columnspan=cols)
                self.col = 0
                self.row += 1
            else:
                ctrl.grid(row=self.row, column=self.col, columnspan=cols)
                self.col += 1

    def _size(self, ctrl, cols):
        '''
        This returns the size of the control, according to the number of columns
        selected.
        '''
        # todo: this is going to be very inaccurate.
        return cols * (self.form_width / self.columns)





