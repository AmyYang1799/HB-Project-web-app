"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb recipes')
os.system('createdb recipes')


model.connect_to_db(server.app)
model.db.create_all()

with open('data/users.json') as f:
    user_data = json.loads(f.read())

# Create users, store them in list so we can use them
# to create recipes later
users_in_db = []
for user in user_data:
    email, password, fname, lname = (user['email'],
                                    user['password'],
                                    user['firstname'],
                                    user['lastname'])
    

    db_user = crud.create_user(email,
                                password,
                                fname,
                                lname)
    users_in_db.append(db_user)