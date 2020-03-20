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




def init():
    print("\nWelcome to your Contact List:\n\n Press 1 to See your Contacts \n Press 2 to Create a new Contact \n Press 3 to Delete a Contact \n Press 4 to Exit\n")
    decide = input("What would you like to do?")


init()

