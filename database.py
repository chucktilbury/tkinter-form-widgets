'''
This is a stub for the database. It exists to allow the formWidgets to be tested. There is no actual
database functionality in this file, but it does provide a template for implementing a real database
that interfaces to the form widgets.
'''

class Database(object):

    __instance = None

    @staticmethod
    def get_instance():
        if Database.__instance == None:
            Database()
        return Database.__instance

    def __init__(self):

        if Database.__instance is None:
            Database.__instance = self
        else:
            raise Exception('The Database class is a singleton. Use get_instance() instead.')

        # put the stuff here to open the database file and all.

    def commit(self):
        '''
        Commit all changes to the database.
        '''

    def read_single_value(self, table, column, row_id):
        '''
        Read a single value from the database.
        '''
        if row_id is None:
            raise Exception('Cannot get item from database: No row ID is set')

        sql = 'SELECT %s FROM %s WHERE ID=%d;'%(column, table, row_id)
        curs = self.execute(sql)
        recs = curs.fetchall()

        retv = None
        for row in recs:
            retv =  row[0]
            break

        return retv

    def write_single_value(self, table, column, row_id, value):
        '''
        Write a single value to the database.
        '''
        vals = tuple([value])
        sql = 'UPDATE %s SET %s=? WHERE ID=%d;'%(table, column, row_id)

        return self.execute(sql, vals)

    def get_column_list(self, table, column):
        '''
        Returns a list of column values in all lines of the table.
        '''
        curs = self.execute('SELECT %s FROM %s;'%(column, table))
        retv = []
        for item in curs:
            retv.append(' '.join(item))
        return retv

    def get_row_id(self, table, column, value):
        '''
        Find the ID of the row that has this column value. If there are
        more than one row that has this value, then the a dictionary of
        the rows is returned. If there are no matches then return None.
        '''
        if type(value) is str:
            sql = 'SELECT ID FROM %s WHERE %s = \"%s\";'%(table, column, value)
        else:
            sql = 'SELECT ID FROM %s WHERE %s = %s;'%(table, column, value)
        row = self.execute(sql).fetchall()

        if len(row) == 0:
            return None
        else:
            return dict(row[0])['ID']

    def get_id_list(self, table, where=None):
        '''
        Get a list of all IDs in a table. This is used (generally) to implement
        next and previous buttons in a form.
        '''
        retv = []
        if where is None:
            sql = 'SELECT ID FROM %s;'%(table)
        else:
            sql = 'SELECT ID FROM %s WHERE %s;'%(table, where)
        cur = self.execute(sql)
        for item in cur:
            retv.append(item[0])

        return retv

    # There will be other functions needed to insert/update rows, delete rows and
    # such, but they are not needed by the form widgets.

    # These functions are stubs that would normally be in the database.
    def execute(self, sql, data = None):
        print('execute: sql = %s, data = %s'%(sql, str(data)))
        return self

    def fetchall(self):
        print('fetchall()')
        return ['x', 'y', 'z']

    def commit(self):
        print('commit()')