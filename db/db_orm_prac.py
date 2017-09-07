#!/usr/bin/env python
# coding:utf-8
# use sqlalchemy module to operate mysql

import os
from random import randrange as rrange
import exceptions
from sqlalchemy import pool, create_engine, Table, Column, String, Integer, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from db_prac import NAMES, randName 
# 提倡先导入Python标准库模块,然后导入第三方或扩展模块,最后导入本地模块的风格

FIELDS = ('login', 'uid', 'prid')
DBNAME = 'testaaa'
PASSWORD = '8169778'
COLSIZ = 10

class MySQLAlchemy(object):
    def __init__(self, db, dbName):
        import MySQLdb
        import _mysql_exceptions
        MySQLdb = pool.manage(MySQLdb)
        url = 'mysql://root:8169778@localhost:3306/%s' % DBNAME
        eng = create_engine(url)
        metadata = MetaData(eng)
#        print '\n'.join(['%s:%s' % item for item in eng.__dict__.items()])
        try:
            cxn = eng.connect()
#            print '\n'.join(['%s:%s' % item for item in cxn.__dict__.items()])
        except OperationalError, e:
            eng1 = create_engine('mysql://root:8169778@localhost:3306')
            DB_Session = sessionmaker(bind = eng1)
            session  = DB_Session() # use it to operarte database
            try:
                session.execute('DROP DATABASE %s' % DBNAME)
            except OperationalError, e:
                pass
            session.execute('CREATE DATABASE %s' % DBNAME)
            session.execute(
            "GRANT ALL ON %s.* TO ''@'localhost' identified by '%s'" % (DBNAME, PASSWORD))
            session.commit() # don't forget to commit
            cxn = eng.connect()

        try:
            users = Table('users', metadata, autoload=True)
        except:
            users = Table('users', metadata,
                Column('login', String(8)),
                Column('uid', Integer),
                Column('prid', Integer),
                )

        self.eng = eng
        self.cxn = cxn
        self.users = users

    def create(self):
        users = self.users
        try:
            users.drop()
        except:
            pass
        users.create()

    def insert(self):
        d = [dict(zip(FIELDS,
        [who, uid, rrange(1,5)])) for who, uid in randName()]
        return self.users.insert().execute(*d).rowcount

    def update(self):
        users = self.users
        fr = rrange(1,5)
        to = rrange(1,5)
        return fr, to, \
    users.update(users.c.prid==fr).execute(prid=to).rowcount

    def delete(self):
        users = self.users
        rm = rrange(1,5)
        return rm, \
    users.delete(users.c.prid==rm).execute().rowcount
 
    def dbDump(self):
        res = self.users.select().execute()
        print '\n%s%s%s' % ('LOGIN'.ljust(COLSIZ),
            'USERID'.ljust(COLSIZ), 'FROJ#'.ljust(COLSIZ))
        for data in res.fetchall():
            print '%s%s%s' % tuple([str(s).title().ljust(COLSIZ) for s in data]) # % requires following a tuple for sure

    def __getattr__(self, attr):
        return getattr(self.users, attr)

    def finish(self):
#        self.cxn.commit()
#        self.eng.close()
        pass

def main():
    print '*** Connecting to %r database' % DBNAME
    orm = MySQLAlchemy('mysql', DBNAME)

    print '\n*** Creating users table'
    orm.create()

    print '\n*** Inserting names into table'
    orm.insert()
    orm.dbDump()

    print '\n*** Randomly moving folks',
    fr, to, num = orm.update()
    print 'from one group (%d) to another (%d)' % (fr, to)
    print '\t(%d users moved)' % num
    orm.dbDump()

    print '\n*** Randomly choosing group',
    rm, num = orm.delete()
    print '(%d) to delete' % rm
    print '\t(%d users removed)' % num
    orm.dbDump()

    print '\n*** Dropping users table'
    orm.drop() # if orm dosen't have method 'drop()', then getattr(orm, 'drop') will be called to delete table.
    orm.finish() # actually,it does nothing.

if __name__ =='__main__':
    main()
