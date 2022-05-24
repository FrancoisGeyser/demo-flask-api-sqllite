from random import randrange
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server import User, UserData, UserProfile

# app
app = Flask(__name__)

# config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

# configure sqlite3 to enforce foreign key contraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


db = SQLAlchemy(app)
db.init_app(app)



def init():
        name = "username"
        password = "password"
        address = "123 fake avenue, your city, your country"
        phone = "+7123456789"
        email = 'username@email.com'
        new_user = User(name=name, password=password)
        db.session.add(new_user)
        db.session.commit()
        new_data =  UserData(address=address, phone=phone, email=email, user_id = new_user.id)
        db.session.add(new_data)
        db.session.commit()

if  __name__ == "__main__":
    init()
