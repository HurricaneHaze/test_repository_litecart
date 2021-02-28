# *-* coding: utf-8 *-*

class Customer:

    def __init__(self, firstname=None, lastname=None, address1=None, postcode=None, city=None, phone=None, email=None,
                 password=None, confirmed_password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address1 = address1
        self.postcode = postcode
        self.city = city
        self.phone = phone
        self.email = email
        self.password = password
        self.confirmed_password = confirmed_password
