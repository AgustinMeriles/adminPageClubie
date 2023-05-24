#!/usr/bin/python3

import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = mysql.connector.connect(
    host='localhost',
    user='AdminClubie',
    password='clubie123',
    database='admin',
)

cursor = db.cursor()

cursor.execute('select * from Usuario')
res = cursor.fetchall()
print(res)


class Club():
    def __init__(self, id_club, name, direction, email, tel, cant):
        self.__id = id_club
        self.name = name
        self.__direction = direction
        self.email = email
        self.__tel = tel
