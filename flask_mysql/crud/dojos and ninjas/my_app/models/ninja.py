from flask import Flask
from my_app.config.mysqlconnection import connectToMySQL, DB
from my_app import app
from my_app.models.dojo import Dojo

class Ninja():
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def add_dojo(cld,data):
        query="insert into ninjas (first_name,last_name,age,created_at,updated_at,dojo_id) values (%(first_name)s,%(last_name)s,%(age)s,now(),now(),%(dojo_id)s) "
        result= connectToMySQL(DB).query_db(query,data) 