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
from select_dialog import SelectDialog

class Forms(tk.LabelFrame):

    def __init__(self, owner, table, columns=4, form_width=700, **kw):
        '''
        owner      = the frame that will own this frame
        table      = table in the database that this form references
        columns    = number of widget columns in the form
        form_width = size of the form in pixels, including buttons
        '''
        super().__init__(owner, **kw)

        self.table = table # database table this form will reference
        self.columns = columns # Number of columns that the form will have
        self.data = Database.get_instance()
        self.owner = owner

        # widget layout information

        # screen factor is the width of a character. Used to convert between
        # pixels and dialog units.
        self.screen_factor = font.Font().measure('x')
        #print('measure', self.screen_factor)

        # Form width in dialog units
        self.form_width = int(form_width / self.screen_factor)
        #print('form width', self.form_width)

        # internal vars for laying out controls
        self.row = 0        # The current row that is being layed out
        self.col = 0        # The current column
        self.ctl_xpad = 5   # horizontal padding for widgets
        self.ctl_ypad = 5   # horizontal padding for widgets

        # button layout information
        self.btn_row = 0    # current row to layout buttons on
        self.btn_xpad = 5   # horizontal padding for buttons
        self.btn_ypad = 5   # verticle padding for buttons
        self.btn_width = 10 # width of all buttons

        # internal frames
        self.btn_frame = tk.Frame(self)
        self.btn_frame.grid(row=0, column=0, sticky='se')
        self.ctl_frame = tk.LabelFrame(self)
        self.ctl_frame.grid(row=0, column=1, sticky='nw')

        # row list management
        self._init_row_list()
        self.row_index = 0

        # controls management
        self.ctl_list = []
        self.grid()

    # Methods that add control widgets to the form
    def add_label(self, text, **kw):
        '''
        Add a dead label to the form. This could be considered part of a control,
        but they are optionally added separately to facilitate lining them up. Labels
        always take up 1 column.
        '''
        widget = tk.Label(self.ctl_frame, text=text, **kw)
        self._grid(widget, 1, sticky='e')

    def add_title(self, text, **kw):
        '''
        A title spans all columns of the form and usually goes at the top or bottom
        of the form.
        '''
        widget = formTitle(self.ctl_frame, text, **kw)
        self._grid(widget, self.columns)

    def add_entry(self, column, cols, _type, **kw):
        '''
        This is the formEntry control.
        '''
        widget = formEntry(self.ctl_frame, self.table, column, _type, **kw)
        self._grid(widget, cols, sticky='w')
        self.ctl_list.append(widget)

    def add_text(self, column, cols, **kw):
        '''
        This is the formText control.
        '''
        widget = formText(self.ctl_frame, self.table, column, **kw)
        self._grid(widget, cols, sticky='w')
        self.ctl_list.append(widget)

    def add_combo(self, column, cols, pop_tab, pop_col, **kw):
        '''
        This is the formCombobox control.
        '''
        widget = formText(self.ctl_frame, self.table, column, pop_tab, pop_col, **kw)
        self._grid(widget, cols, sticky='w')
        self.ctl_list.append(widget)

    def add_dynamic_label(self, column, cols, **kw):
        '''
        This is the formDynamicLabel control.
        '''
        widget = formDynamicLabel(self.ctl_frame, self.table, column, **kw)
        self._grid(widget, cols, sticky='w')
        self.ctl_list.append(widget)

    def add_indirect_label(self, column, cols, rem_tab, rem_col, **kw):
        '''
        This is the formIndirectLabel control.
        '''
        widget = formIndirectLabel(self.ctl_frame, self.table, column, **kw)
        self._grid(widget, cols, sticky='w')
        self.ctl_list.append(widget)

    def add_checkbox(self, column, cols, **kw):
        '''
        This is the formCheckbox control.
        '''
        widget = formCheckbox(self.ctl_frame, self.table, column, **kw)
        self._grid(widget, cols, sticky='w')
        self.ctl_list.append(widget)

    def add_custom_widget(self, cols, cls, **kw):
        '''
        This is any widget that has a self-contained class.
        '''
        widget = cls(**kw)
        self._grid(widget, cols, sticky='w')
        self.ctl_list.append(widget)

    def add_spacer(self, cols):
        '''
        This is an empty tk.Frame to simply take up spade.
        '''
        widget = tk.Frame(self.ctl_frame)
        self._grid(widget, cols)


    # Methods that add button widgets to the form
    def add_ctl_button(self, title, column=None, class_name=None, thing=None, new_flag=False, **kw):
        '''
        This adds a known control button to the form.
        '''
        if title == 'Next':
            command = self._next_btn
        elif title == 'Prev':
            command = self._prev_btn
        elif title == 'Prev':
            command = self._prev_btn
        elif title == 'Clear':
            command = self._clear_btn
        elif title == 'Delete':
            command = self._delete_btn
        elif title == 'Save':
            command = lambda f=new_flag: self._save_btn(f)
        elif title == 'New':
            if class_name is None:
                raise Exception("New button requires a class to be specified.")
            command = lambda c=class_name: self._new_btn(c)
        elif title == 'Edit':
            if class_name is None:
                raise Exception("Edit button requires a class to be specified.")
            command = lambda c=class_name: self._edit_btn(c)
        elif title == 'Select':
            if column is None:
                raise Exception("Select button requires a column to be specified.")
            command = lambda c=column, t=thing: self._select_btn(c, t)
        else:
            raise Exception("Unknown control button type: %s"%(title))

        widget = tk.Button(self.btn_frame, text=title, width=self.btn_width, command=command, **kw)
        widget.grid(row=self.btn_row, column=0, padx=self.btn_xpad, sticky='nw')
        self.btn_row += 1

    def add_custom_button(self, cls, **kw):
        '''
        This adds a custom button from a self-contained class.
        '''
        widget = cls(self.btn_frame, **kw)
        widget.grid(row=self.btn_row, column=0, padx=self.btn_xpad, sticky='nw')
        self.btn_row += 1

    def add_btn_spacer(self):
        '''
        Adds a space between buttons.
        '''
        widget = tk.Frame(self.btn_frame)
        widget.grid(row=self.btn_row, column=0, pady=self.btn_ypad, sticky='nw')
        self.btn_row += 1


    # Methods that control the form
    def load_form(self):
        '''
        Call all of the setter functions for all of the widgets.
        '''
        if len(self.row_list) == 0:
            showinfo('Records', 'There are no records to show for this form.')
            return

        for item in self.ctl_list:
            item.set_row_id(self._row_id())
            item.setter() # set the widget value
            item.is_changed(True) # reset the changed flag

    def save_form(self, new_flag=False):
        '''
        Call all of the getter functions for all of the widgets.
        '''
        if new_flag:
            data = {}
            for item in self.ctl_list:
                key, val = item.get_insert_value()
                data[key] = val
            self.data.insert_row(self.table, data)
            self._init_row_list()
            self.row_index = len(self.row_list)-1
        else:
            if len(self.row_list) == 0:
                showinfo('Records', 'There are no records to save for this form.')
                return
            else:
                for item in self.ctl_list:
                    item.set_row_id(self._row_id())
                    if item.is_changed(True):
                        item.getter() # get the widget value
        self.data.commit()

    def show_form(self):
        '''
        Load the current row into the form and then place it in the owner's
        grid.
        '''
        self.grid()
        self.load_form()

    def hide_form(self):
        '''
        Call grid_forget() on this form.
        '''
        self.grid_forget()

    # Standard button callbacks
    def _next_btn(self):
        '''
        Get the next row in the table and load the form.
        '''
        for item in self.ctl_list:
            if item.is_changed():
                if askyesno('Save This?', 'There are changed fields. Do you want to save this record?'):
                    self.save_form()
                break

        if not self.row_list is None:
            self.row_index += 1
            if self.row_index > len(self.row_list)-1:
                self.row_index = len(self.row_list)-1
                showinfo('Last Record', 'This is the last record.')
            else:
                self.load_form()

    def _prev_btn(self):
        '''
        Get the previous row in the database and load the form.
        '''
        for item in self.ctl_list:
            if item.is_changed():
                if askyesno('Save This?', 'There are changed fields. Do you want to save this record?'):
                    self.save_form()
                break

        if not self.row_list is None:
            self.row_index -= 1
            if self.row_index < 0:
                self.row_index = 0
                showinfo('First Record', 'This is the first record.')
            else:
                self.load_form()

    def _clear_btn(self):
        '''
        Clear the form or open the edit dialog.
        '''
        for item in self.ctl_list:
            item.clear()

    def _save_btn(self, new_flag=False):
        '''
        Call all of the getter functions for all of the controls and
        commit the database changes.
        '''
        if askyesno('Save record?', 'Are you sure you want to save this?'):
            self.save_form(new_flag)

    def _delete_btn(self):
        '''
        Delete the current row from the database and load the next one.
        '''
        if askyesno('Delete record?', 'Are you sure you want to delete this?'):
            self.data.delete_row(self.table, self.row_list[self.row_index])
            self.data.commit()

            self.row_list = self.data.get_id_list(self.table)
            if self.row_index > len(self.row_list):
                self.row_index -= 1
            self.load_form()

    def _edit_btn(self, _class):
        '''
        Call up the edit dialog for this table row.
        '''
        _class(self.owner, self.row_index)
        self.load_form()

    def _select_btn(self, column, thing=None):
        '''
        Open the select dialog and select from the column in the row.
        '''
        sd = SelectDialog(self.owner, self.table, column, thing)
        #print(sd.item_id)
        if sd.item_id > 0:
            self.row_index = self.row_list.index(sd.item_id)
            self.load_form()

    def _new_btn(self, _class):
        '''
        Simply create a new table record and store it in the database.
        '''
        _class(self.owner)
        self._init_row_list()

    # Other private functions
    def _get_geometry(self, wid):
        # Note that this does not work on frames or empty widgets.
        wid.update()
        return {'width':wid.winfo_width(), 'height':wid.winfo_height(),
                'hoffset':wid.winfo_x(), 'voffset':wid.winfo_y(),
                'name':wid.winfo_name()}

    def _grid(self, ctrl, cols, **kw):
        '''
        This calls the grid function on the control and sets it in the proper
        location with the proper size.
        '''
        # will this fit into the columns available?
        if self.col + cols <= self.columns:
            # yes put it in the location
            ctrl.grid(row=self.row, column=self.col,
                        columnspan=cols,
                        padx=self.ctl_xpad, pady=self.ctl_ypad, **kw)
            self.col += cols
        else:
            # no move it down a row
            self.col = 0
            self.row += 1
            ctrl.grid(row=self.row, column=self.col,
                        columnspan=cols,
                        padx=self.ctl_xpad, pady=self.ctl_ypad, **kw)
            self.col += cols

    def _row_id(self):
        '''
        Return the current row_id
        '''
        #print('list:', self.row_list, 'index:', self.row_index)
        if self.row_list is None:
            return 0
        return self.row_list[self.row_index]

    def _init_row_list(self):
        '''
        Create the row list.
        '''
        #print('init_row_list')
        if self.table is None:
            self.row_list = None # getting the row list might be deferred
        else:
            self.row_list = self.data.get_id_list(self.table)

