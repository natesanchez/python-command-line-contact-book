from peewee import *

db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port='5432')

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    firstname = CharField()
    lastname = CharField()
    phone = CharField()
    email = CharField()


db.connect()


db.create_tables([Contact])

nate = Contact(firstname="Nate", lastname="Sanchez", phone="7733197218", email="nsanchez@usa.com")
nate.save()


def init():
    print("\nContact Book:\n\n Enter 1 to See your Contacts \n Enter 2 to Create a new Contact \n Enter 3 to Delete a Contact \n Enter 4 to Exit\n")
    option = input("What would you like to do?: ")
    if option == "1":
        display()
    elif option == "2":
        create()
    elif option == "3":
        delete()
    elif option == "4":
        exit()
    else:
        print("Please Select a Valid Option")
        init()


def display():
    contacts = Contact.select()
    for contact in contacts:
            print(f' \n Full Name: {contact.firstname} {contact.lastname}\n phone: {contact.phone}\n email: {contact.email}\n')
    back = input("Here are all your contacts! would you like to go back to the selection page? y/n: ")
    if back == "y":
        init()
    else:
        exit()






init()

