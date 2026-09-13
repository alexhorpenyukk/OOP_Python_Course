#################
## CHALLENGE 3 ##
#################

# Requirements:
# - Define a new type called Contact, which should store a person's name, last name, phone, email, as well as an
# instance attribute called display_mode, which defaults to "masked"
# - Should be able to create instances using name and last name only
# - Two instances should be considered equal if any of the following conditions are met:
#     - name, last name, phone and email are the same, or
#     - phone or email are the same
# - The instance representation should return obfuscated name and last name attributes when display_mode is set to "masked"
# and the regular full representation including all attributes otherwise
# - The str() representation on the other hand should always return the first letter of the last name followed by the
# first letter of the first name
# - A user should be able to format a masked instance's string representation so as to reveal all the attributes

# Example Usage:
# c1 = Contact("Andy", "Bek")
# c2 = Contact("Andy", "Bek", "647-537-9271")
# c3 = Contact("Andrew", "Bek", "647-537-9271", "hey@andybek.com")
# c4 = Contact("Andy", "Bek", "647-537-9271", display_mode="show")

# c2 == c3
# True # because the phone number is the same

# c1
# Contact(name=An***, last_name=B**)

# str(c1)
# 'BA'

# "{c:unmasked}".format(c=c1)
# 'Contact(name=Andy, last_name=Bek, phone=None, email=None)'

# f"{c2:unmasked}"
# 'Contact(name=Andy, last_name=Bek, phone=647-537-9271, email=None)'

# format(c2, "unmasked")
# 'Contact(name=Andy, last_name=Bek, phone=647-537-9271, email=None)'

class Contact():
    def __init__(self, name, last_name, phone = None, email = None, dispay_mode = 'masked'):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.dispay_mode = dispay_mode

    def __eq__(self, other):
        return ((self.phone != None and self.phone == other.phone) or (self.email != None and self.email == other.email)) or (self.name == other.name and self.last_name == other.last_name)
    
    def __repr__(self):
        if self.dispay_mode == 'masked':
            masked_name = self.name[0 : len(self.name)//2] + '*' * round(len(self.name) / 2)
            masked_last_name =self.last_name[0 : len(self.last_name)//2] + '*' * round(len(self.last_name) / 2)
            return f"Contact('{masked_name}', '{masked_last_name}')"
        return f"Contact('{self.name}', '{self.last_name}', '{self.phone}', '{self.email}')"
    
    def __str__(self):
        return f'{self.last_name[0]}. {self.name[0]}.'
    
    def __format__(self, format_spec):
        if format_spec == 'unmasked':
            return f"Contact('{self.name}', '{self.last_name}', '{self.phone}', '{self.email}')"
