from peewee import *

database = SqliteDatabase('DocDb.db', **{})

class UnknownField(object):

    def __init__(self, *_, **__): pass

class BaseModel(Model):

    class Meta:

        database = database

class Doc(BaseModel):

    data = BlobField()

    name = TextField()

    class Meta:

        table_name = 'doc'

class SqliteSequence(BaseModel):

    name = UnknownField(null=True)  # 

    seq = UnknownField(null=True)  # 

    class Meta:

        table_name = 'sqlite_sequence'
        
        primary_key = False

