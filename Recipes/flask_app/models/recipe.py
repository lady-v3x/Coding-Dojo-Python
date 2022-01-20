from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under30 = data['under30']
        self.madeOn = data['madeOn']
        self.user_id = data['user_id']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        
    @classmethod
    def save(cls, data):
        query="INSERT INTO recipes (name, description, instructions, under30, madeOn, user_id, createdAt, updatedAt) VALUES (%(name)s, %(description)s, %(instructions)s, %(under30)s, %(madeOn)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL('recipes_schema').query_db(query,data)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_schema').query_db(query)
        recipes = []
        for row in results:
            recipes.append( cls(row))
        return recipes
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(recipe.id)s;"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        return cls(results[0])
    @classmethod
    def update(cls, data):
        query="UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under30 = %(under30)s, madeOn = %(madeOn)s, updatedAt = NOW() WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query,data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","recipe")
        if len(recipe['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters","recipe")
        if len(recipe['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","recipe")
        if recipe['madeOn'] == "":
            is_valid = False
            flash("Please enter a date","recipe")
        return is_valid