###############################################################################
#
#   This is the test database used to test the form widgets.
#

CREATE TABLE Contact
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address1 TEXT,
        address2 TEXT,
        state TEXT,
        city TEXT,
        zip TEXT,
        email_address TEXT NOT NULL,
        phone_number TEXT,
        web_site TEXT,
        description TEXT,
        country TEXT);
