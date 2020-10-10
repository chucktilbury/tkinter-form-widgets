import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
from tkinter.messagebox import *
from database import Database
from form_widgets import toolTip

class searchWidget(ttk.Combobox):

    def __init__(self, owner, table, column, tool_tip=None, **kw):
        super().__init__(owner, **kw)

        self.table = table
        self.column = column
        if not tool_tip is None:
            self.ttip = toolTip(self, tool_tip)

        self.bind('<Key>', self._key_handler)
        self.data = Database.get_instance()

        self.key = ''
        self.lst = self._generate_list()
        #self.lst.sort()
        self.values = self.lst

        #self.values = ['value1', 'value2', 'value3', 'value4', 'value5']

    def _key_handler(self, event=None):
        print(event, self.get())
        # if event.char >= '0' and event.char <= '9' \
        #         or event.char >= 'a' and event.char <= 'z' \
        #         or event.char >= 'A' and event.char <= 'Z':
        #     self.key += event.char
        # elif event.char == '%':
        #     self.key += '%'
        # elif event.char == '\x08':
        #     self.key = self.key[:-1]

        self._generate_list()

    def _generate_list(self):
        #newkey = self.key + '%'
        newkey = self.get() + '%'
        line = 'SELECT %s FROM %s WHERE %s LIKE \'%s\''%(self.column, self.table, self.column, newkey)

        cur = self.data.execute(line)
        lst = []
        #lst.append(self.key)

        try:
            for item in cur:
                lst.append(item[0])
        except:
            print('exception')
            pass

        print(lst)
        self['values'] = lst
