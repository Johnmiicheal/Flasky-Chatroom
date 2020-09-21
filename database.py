"""Automated database query management"""

import sqlite3

database = sqlite3.connect("chat.db")
cursor = database.cursor()


""" This initializes the database table, so run once and comment it out """
#create_users_sql = "CREATE TABLE users (username TEXT, real_name TEXT)"
#cursor.execute(create_users_sql)

database.commit()
database.close()


class Database:
    def __init__(self):
        self.database = "chat.db"

    def perform_insert(self, sql, params):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()   

    def perform_select(self, sql, params):
        conn = sqlite3.connect(self.database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(sql, params)
        results = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return results

    def add_user(self, username, real_name):
        sql = "INSERT INTO users (username, real_name) VALUES (?, ?)"
        query_params = (username, real_name)

        self.perform_insert(sql, query_params)

    def get_all_users(self):
        sql_chat = "SELECT username, real_name FROM users"
        params = []

        return self.perform_select(sql_chat, params) 

    def user_exists(self, username):
        sql = "SELECT username FROM users WHERE username = ?"
        params = (username)

        results = self.perform_select(sql, params)
        if len(results):
            return True

        return False


        


