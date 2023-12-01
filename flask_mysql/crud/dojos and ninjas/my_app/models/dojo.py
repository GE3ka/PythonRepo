from flask import Flask
from my_app.config.mysqlconnection import connectToMySQL, DB
from my_app import app

class Dojo():
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def display_dojos(cls):
        query= "select * from dojos;"
        results= connectToMySQL(DB).query_db(query)  
        dojos=[]
        for row in results:
            dojos.append(Dojo(row))
        return dojos
    @classmethod
    def add_dojo(cls,data):
        query="insert into dojos (name,created_at,updated_at) values (%(name)s,now(),now());" 
        result= connectToMySQL(DB).query_db(query,data) 

    @classmethod
    def show_dojo(cls,data):
        ninjas=[]
        query="select * from ninjas join dojos on ninjas.dojo_id=dojos.id where dojos.id= %(id)s;"
        result=connectToMySQL(DB).query_db(query,data)
        
        for ninja in result:
            ninjas.append(ninja)
        return(ninjas)        


