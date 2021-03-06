#! /usr/bin/env python

from FightingFantasy import app, db
from FightingFantasy.models import User
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username='paddy', email='outlawgames@gmail.com'))
    db.session.commit()
    print 'Initialized the database'

@manager.command
def dropdb():
    if prompt_bool('Are you sure you want to lose all your data'):
        db.drop_all()
        print 'Dropped the database'

if __name__ == '__main__':
    manager.run()