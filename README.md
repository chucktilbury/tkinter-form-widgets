# Form widgets for tkinter and sqlite3
These classes are intended to be the core for any application that needs to represent database tables as forms. The forms are generic and can be used in any kind of tkinter.Frame.

Only widgets that present a value that can be stored in a database are presented. These widget classes are used exactly like a regular tkinter widget would be used, but with some extra parameters for database access.

This uses the Sqlite3 database, but any SQL database should be easily interfaced by replacing parts of the Database class.

The forms are created as a single stand-alone widget with completely internal event handling.

Only Python 3.x is supported.

## Demo application
The library is presented as an implementation of a contacts database. It is not really intended to be useful for that, but instead, to demonstrate and test the library functionality.

## Supported tkinter widgets
Only widgets that may have data in a database are supported. This is a bare minimum that one may use for forms.

All of these widgets implement functions to get and save data to the database.
* getter() -- Reads the widget and saves the data to the database.
* setter() -- Reads the database and places the data into the widget.
* clear() -- Removes the data from the widget. Does not update the database. For the combo box, it resets the selection.
* populate() -- For the combo box widget, this populates the items in it from the database. For other widgets, it simply does the same thing as setter()

### formEntry
This wraps the tkinter Entry class. The getter function automatically casts return value to the type used by the database.

##### Additional parameters
* table -- This is the table that the data for this widget is in.
* column -- This is the column of the table.
* type -- This is the type of the data as it appears in the database.

### formText
This class wraps the tkinter Text class. It provides horizontal and verticle scroll bars for the text.

##### Additional parameters
* table -- This is the table that the data for this widget is in.
* column -- This is the column of the table.

### formDynamicLabel
An dynamic label wraps the tkinter Label class. A dynamc label is one that simply has an entry in the database. The getter function does not do anything because the item cannot be edited. The setter and populate function work as expected.

##### Additional parameters
* table -- This is the table that the data for this widget is in.
* column -- This is the column of the table.

### formIndirectLabel
An indirect label wraps the tkinter Label class. An indirect label is one where the database entry is an ID for an entry in another table. So, the setter and getter must first find that entry before reading or writing to the widget.

##### Additional parameters
* loc_table -- This is the local table that the data for this widget is in.
* loc_column -- This is the column of the local table.
* rem_table -- This is the remote table where the data that will be displayed is located.
* rem_column -- This is the column of the remote table.

### formCombobox
This is a wrapper for the tkinter.ttk Combobox widget. In the local table, an ID is stored for a string to display that is in a remote table. All of the rows in the remote table that have an entry for the remote column are read and used as entries for the combo box. Note that the populate function must be called when this widget is first displayed. If the list of strings is going to change, then populate must be called every time that happens.

##### Additional parameters
* loc_table -- This is the local table that the data for this widget is in.
* loc_column -- This is the column of the local table.
* rem_table -- This is the remote table where the data that will be displayed is located.
* rem_column -- This is the column of the remote table.

### formCheckbox
This is a wrapper for the tkinter Checkbox class. The check box represents a boolean value in the database.

##### Additional parameters
* table -- This is the table that the data for this widget is in.
* column -- This is the column of the table.

### formTitle
This is a wrapper for the Label tkinter class. It provides a way to add enlarged text to a form without having to think about the font size, etc.

##### Additional parameters
none
