from peewee import *
from datetime import date

db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port='5432')

class BaseModel(Model):

    class Meta:
        database = db

class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    birthday = DateField()
    phone = CharField()
    email = CharField()
    address = CharField()
 
db.connect()
db.drop_tables([Contact])
db.create_tables([Contact])
 
def hello():
    print('Contact Book COntrols \n 1: See Contacts \n 2: Make Contact \n 3: Update Contact \n 4: Delete Contact \n 5: Exit')
    greet = input('Enter the number of what you want to do: ')
    if greet == '1':
        show_contact()
    elif greet == '2':
        create_contact()
    elif greet == '3':
        update()
    elif greet == '4':
        delete()
    else:
        print('Bye Felicia')
        exit()

def show_contact():
    contacts = Contact.select()
    for contact in contacts:
        print(contact.first_name)
    show = input("Enter name for full info \nCase sensitive \nOr 'q' to go back to main menu: ")
    if show == 'q':
        hello()
    contact = Contact.get(Contact.first_name == show)
    print(f' Full Name: {contact.first_name} {contact.last_name} \n Birthday: {contact.birthday} \n Phone Number: {contact.phone} \n Email: {contact.email} \n Address: {contact.address}')
    show_contact()

def create_contact():
    new_first_name = input('Insert First Name: ')
    new_last_name = input('Insert Last Name: ')
    new_birthday = input('Insert Birthday: ')
    new_phone = input('Insert Phone Number: ')
    new_email = input('Insert Email: ')

    add_contact = Contact(
        first_name = new_first_name,
        last_name = new_last_name,
        birthday = new_birthday,
        phone = new_phone,
        email = new_email,
    )
    add_contact.save()
    hello()

def update():
    contacts = Contact.select()
    for contact in contacts:
        print(contact.first_name)
    ask1 = input('Enter name of contact to update \nCase Sensitive: ')
    if ask1 == Contact.first_name:
        print(' 1: First name \n 2: Last name \n 3: Birthday \n 4: Phone number \n 5: Email')
        ask2 = input('Enter number of subject to update: ')
        if ask2 == '1':
            contact = Contact.get(Contact.first_name == ask1)
            contact.first_name = input('New first name: ')
            contact.save()
            hello()
        elif ask2 == '2':
            contact = Contact.get(Contact.first_name == ask1)
            contact.last_name = input('New last name: ')
            contact.save()
            hello()
        elif ask2 == '3':
            contact = Contact.get(Contact.first_name == ask1)
            contact.birthday = input('New birthday: ')
            contact.save()
            hello()
        elif ask2 == '4':
            contact = Contact.get(Contact.first_name == ask1)
            contact.phone = input('New phone number: ')
            contact.save()
            hello()
        elif ask2 == '5':
            contact = Contact.get(Contact.first_name == ask1)
            contact.email = input('New email: ')
            contact.save()
            hello()
        else:
            hello()

def delete():
    contacts = Contact.select()
    for contact in contacts:
        print(contact.first_name)
    bye = input('Pick which contact to delete: ')
    if bye == Contact.first_name:
        sure = input('Are you sure you want to delete this Dirtbag? y/n: ')
        if sure == 'y':
            contact = Contact.get(Contact.first_name == bye)
            contact.delete_instance()
            hello()
        else:
            delete()
    else:
        hello()

hello()