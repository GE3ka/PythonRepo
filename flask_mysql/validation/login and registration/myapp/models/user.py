from flask import Flask
from myapp.config.mysqlconnection import connectToMySQL, DB
from myapp import app
import re
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)

class User():

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    def __init__(self,data):
        self.id =data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls,data):
        encrypted_password = bcrypt.generate_password_hash(data['password'])
        data = dict(data)
        data['password'] = encrypted_password

        query = "insert into users (first_name,last_name,email,password,created_at,updated_at) values (%(first_name)s,%(last_name)s,%(email)s,%(password)s,now(),now());"
        result=connectToMySQL(DB).query_db(query,data)
        return result
    
    @classmethod
    def getuser_by_email(cls,data):
        query="select *  from users where email = %(email)s"
        result = connectToMySQL(DB).query_db(query,data)
        if result:
            return cls(result[0])
        return False
    
    @staticmethod
    def validation(data):
        is_valide=True
        user_found = User.getuser_by_email(data)
        if len(data['first_name'])<2:
            flash("First name is invalide")
            is_valide = False
        if len(data['last_name'])<2:
            flash("Last Name is invalide")  
            is_valide = False
        if not User.EMAIL_REGEX.match(data['email']):
            flash("Invalid email format.")
            is_valide = False 
        if user_found:
            flash("Email already exists")
            is_valide = False  
        if len(data['password'])<8:
            flash ("Password must contain 8 characters or more") 
            is_valide = False
        if data['password'] != data['password_confirmation'] :
            flash("The passwords does not match") 
            is_valide =  False
        return is_valide

    @staticmethod
    def login_validation(data):
        is_valide = True
        user_found = User.getuser_by_email(data)
        if not User.EMAIL_REGEX.match(data['email']):
            flash("Login: Invalid email format.")
            is_valide = False
        if not user_found:
            flash("User with this email is not found")
            is_valide = False
        if user_found:  
            if len(data['password']) <=0:
                flash("Password cannot be empty") 
                is_valide=False
            else:
                if not bcrypt.check_password_hash(user_found.password, data['password']):
                    flash("Incorrect Password")
                    is_valide = False  
        return is_valide                       

