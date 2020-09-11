# Form widgets for tkinter and sqlite3 
This is a simple wrapper that allows tkinter form widgets to access a sqlite3 database to get and store values. Only widgets that present a value that can be stored in a database are presented. These widget classes are used exactly like a regular tkinter widget would be used, but with some extra parameters for database access.

Only Python 3.x is supported. 

### Supported tkinter widgets
Only widgets that may have data in a database are supported. This is a bare minimum that one may use for forms.

All of these widgets implement functions to get and save data to the database.
* getter() -- Reads the widget and saves the data to the database. 
* setter() -- Reads the database and places the data into the widget.
* clear() -- Removes the data from the widget. Does not update the database. For the combo box, it resets the selection.
* populate() -- For the combo box widget, this populates the items in it from the database. For other widgets, it simply does the same thing as setter()

#### formEntry
This wraps the tkinter Entry class. The getter function automatically casts return value to the type used by the database.

##### Additional parameters
* table -- This is the table that the data for this widget is in.
* column -- This is the column of the table.
* type -- This is the type of the data as it appears in the database.

#### formText
This class wraps the tkinter Text class. It provides horizontal and verticle scroll bars for the text.

##### Additional parameters
* table -- This is the table that the data for this widget is in.
* column -- This is the column of the table.

#### formDynamicLabel
An dynamic label wraps the tkinter Label class. A dynamc label is one that simply has an entry in the database. The getter function does not do anything because the item cannot be edited. The setter and populate function work as expected.

##### Additional parameters
* table -- This is the table that the data for this widget is in.
* column -- This is the column of the table.

#### formIndirectLabel
An indirect label wraps the tkinter Label class. An indirect label is one where the database entry is an ID for an entry in another table. So, the setter and getter must first find that entry before reading or writing to the widget.

##### Additional parameters
* loc_table -- This is the local table that the data for this widget is in.
* loc_column -- This is the column of the local table.
* rem_table -- This is the remote table where the data that will be displayed is located.
* rem_column -- This is the column of the remote table.

#### formCombobox
This is a wrapper for the tkinter.ttk Combobox widget. In the local table, an ID is stored for a string to display that is in a remote table. All of the rows in the remote table that have an entry for the remote column are read and used as entries for the combo box. Note that the populate function must be called when this widget is first displayed. If the list of strings is going to change, then populate must be called every time that happens.

##### Additional parameters
* loc_table -- This is the local table that the data for this widget is in.
* loc_column -- This is the column of the local table.
* rem_table -- This is the remote table where the data that will be displayed is located.
* rem_column -- This is the column of the remote table.



