from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'recipes_schema'

class Recipe:
    
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        if 'first_name' in data:
            self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for result in results:
            recipes.append(Recipe(result))
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id=%(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return Recipe(result[0])

    @classmethod
    def get_one_with_join(cls, data):
        query = "SELECT * FROM recipes_schema.recipes join users on recipes.user_id  = users.id where recipes.id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return Recipe(result[0])

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Recipe name must be at least 3 characters")
            is_valid = False     
        if len(recipe['description']) < 3:
            flash("description must be at least 3 characters")
            is_valid = False     
        if len(recipe['instructions']) < 3:
            flash("instructions must be at least 3 characters!!!")
            is_valid = False     
        if len(recipe['date_made']) < 2:
            flash("you messed up the date try again!!!")
            is_valid = False     
        # if len(recipe['under_30']) < 2:
        #     flash("you messed up, try again!!!", "first_name")
        #     is_valid = False     
        return is_valid

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes where id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data )