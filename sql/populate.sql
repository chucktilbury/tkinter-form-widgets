###############################################################################
#
#   This is the test database used to test the form widgets.
#

INSERT INTO Contact
        (name, address1, address2, city, state, zip, email_address,
        phone_number, web_site, description, country)
    VALUES
        ('Chuck Tilbury',
        '1085 State Highway 99', NULL,
        'Green Hills', 'Oklahoma', '74923',
        'info@whistlemaker.com',
        '+1-918-647-8322',
        'http://whistlemaker.com',
        'Author of this library.',
        'United States');

INSERT INTO Contact
        (name, address1, address2, city, state, zip, email_address,
        phone_number, web_site, description, country)
    VALUES
        ('Furd Smeddly',
        '1234 Snide Estate Rd', NULL,
        'Renkovic', NULL, '80808-12',
        'furd@smeddly.com',
        '+03-840-8322',
        'http://furdsmeddly.com',
        NULL,
        'Norway');

INSERT INTO Contact
        (name, address1, address2, city, state, zip, email_address,
        phone_number, web_site, description, country)
    VALUES
        ('Carl Smith',
        '185 Glib Rd', 'Apt. 12',
        'Houston', 'Texas', '78556',
        'carl1922@grope.com',
        '+1-713-802-8922',
        NULL,
        NULL,
        'United States');

INSERT INTO Contact
        (name, address1, address2, city, state, zip, email_address,
        phone_number, web_site, description, country)
    VALUES
        ('Knuckles Pendragon',
        '1 Loo St', 'Apartment 3',
        'Glaskow', 'Rotter', '953-123',
        'kpendragon@msn.com',
        '+02-123-4567',
        'http://dragons.com',
        'Smarter, younger, faster brother of Arthur',
        'Scotland');

INSERT INTO Contact
        (name, address1, address2, city, state, zip, email_address,
        phone_number, web_site, description, country)
    VALUES
        ('Ferd Smeddly',
        NULL, NULL,
        NULL, NULL, NULL,
        'ferdsmedd@msn.com',
        NULL,
        NULL,
        NULL,
        NULL);

INSERT INTO Contact
        (name, address1, address2, city, state, zip, email_address,
        phone_number, web_site, description, country)
    VALUES
        ('Fred Flinstone',
        '301 Cobblestone Way', NULL,
        'Slaughter', 'Sheepstone', '70777',
        'fflintstone@msnstone.com',
        NULL,
        NULL,
        "Member of Loyal Order of Water Buffaloes in food standing.
Member of fictional characters that actually lived secret society.
Member of Hollyrock actors guild.",
        NULL);

INSERT INTO Contact
        (name, address1, address2, city, state, zip, email_address,
        phone_number, web_site, description, country)
    VALUES
        ('Wilma Flinstone',
        '301 Cobblestone Way', NULL,
        'Slaughter', 'Sheepstone', '70777',
        'wflintstone@msnstone.com',
        NULL,
        NULL,
        'Member of Hollyrock actors guild.',
        NULL);

