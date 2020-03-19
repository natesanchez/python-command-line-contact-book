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





