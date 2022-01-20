from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self,data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.pw = data['pw']
        self.pwConfirm = data['pwConfirm']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        
    @classmethod
    def newUser(cls, data):
        query="INSERT INTO users (firstName, lastName, email, pw, pwConfirm, createdAt, updatedAt) VALUES (%(firstName)s, %(lastName)s, %(email)s, %(pw)s, %(pwConfirm)s, NOW(), NOW());"
        return connectToMySQL('recipes_schema').query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('recipes_schema').query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users

    @classmethod
    def get_by_email(cls, data):
        query="SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        return cls(results[0])    
    
    @staticmethod
    def is_valid(user):
        is_valid = True
        query="SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('recipes_schema').query_db(query,user)
        if len(user['firstName']) < 2:
            is_valid = False
            flash("First name must be at least 2 characters.")
        if len(user['lastName']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters.")
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email.")
            is_valid=False    
        if len(user['pw']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters long.")
        if user['pwConfirm'] != user['pw']:
            is_valid = False
            flash("Passwords do not match.")
        return is_valid