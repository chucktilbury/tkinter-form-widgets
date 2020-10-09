
from forms import Forms
from contact_edit import ContactEdit, NewContact

class ContactForm(Forms):

    def __init__(self, owner):
        '''
        This form displays the data as read-only labels.
        '''
        super().__init__(owner, 'Contact', columns=4)

        self.width1 = 70
        self.width2 = 30

        self.add_title('Contacts')

        self.add_label('Name:')
        self.add_dynamic_label('name', 3, bg='white', width=self.width1, anchor='w')

        self.add_label('Address1:')
        self.add_dynamic_label('address1', 3, bg='white', width=self.width1, anchor='w')

        self.add_label('Address2:')
        self.add_dynamic_label('address2', 3, bg='white', width=self.width1, anchor='w')

        self.add_label('City:')
        self.add_dynamic_label('city', 1, bg='white', width=self.width2, anchor='w')

        self.add_label('State:')
        self.add_dynamic_label('state', 1, bg='white', width=self.width2, anchor='w')

        self.add_label('Post Code:')
        self.add_dynamic_label('zip', 1, bg='white', width=self.width2, anchor='w')

        self.add_label('Country:')
        self.add_dynamic_label('country', 1, bg='white', width=self.width2, anchor='w')

        self.add_label('Email:')
        self.add_dynamic_label('email_address', 1, bg='white', width=self.width2, anchor='w')

        self.add_label('Phone:')
        self.add_dynamic_label('phone_number', 1, bg='white', width=self.width2, anchor='w')

        self.add_label('Web Site:')
        self.add_dynamic_label('web_site', 3, bg='white', width=self.width1, anchor='w')

        self.add_label('Description:')
        self.add_dynamic_label('description', 3, bg='white', height=20, width=self.width1, anchor='nw', justify='left')

        self.add_ctl_button('Next')
        self.add_ctl_button('Prev')
        self.add_btn_spacer()
        self.add_ctl_button('New', class_name=NewContact)
        self.add_ctl_button('Select', column='name', thing='Contact')
        self.add_ctl_button('Edit', class_name=ContactEdit)
        self.add_ctl_button('Delete')
        self.load_form()

