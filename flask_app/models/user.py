import re  # the regex module
from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "new_users_cr"


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s , %(last_name)s , %(email)s )"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
