#!/usr/bin/env python
# coding:utf8

from sqlalchemy import *
from sqlalchemy.orm import *
#from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql://root:8169778@localhost:3306/testaaa')
metadata = MetaData(engine)

user = Table('user', metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String(20)),
    Column('fullname', String(40)))
address = Table('address', metadata, 
    Column('id', Integer, primary_key = True),
    Column('user_id', None, ForeignKey('user.id')), 
    Column('email', String(60), nullable = False),
)
metadata.create_all(engine)
conn = engine.connect()
