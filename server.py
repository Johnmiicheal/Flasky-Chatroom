from flask import Flask, jsonify, request
from database import Database
from conversation import Conversation
import os





app = Flask(__name__)
app.config.from_object(__name__)

conversations_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'conversation.py'))
database = Database()

@app.route("/")
def index():
    return "Welcome to Index"

@app.route("/add_user")
def add_user():
    data = request.form
    username = data["username"]
    full_name = data["real_name"]
    database.add_user(username, full_name)

    return jsonify(
        "User Created"
    )

@app.route("/get_all_users")
def get_all_users():
    all_users = database.get_all_users()

    return jsonify(all_users)

@app.route("/user_exists", methods=["POST"])
def user_exists():
    username = request.form.get("username")
    exists = database.user_exists(username)

    return jsonify({
        "exists": exists
    })

def get_conversation_db_path_for_users(data):
    user_one = data["user_one"]
    user_two = data["user_two"]

    users_in_order = sorted([user_one, user_two])
    users_in_order = "_".join(users_in_order)

    conversations_db = users_in_order + ".db"
    conversations_db_path = os.path.join(conversations_dir, conversations_db)

    return conversations_db_path

@app.route("/create_conversation_db", methods=["POST"])
def create_conversation_db():
    conversations_db_path = get_conversation_db_path_for_users(request.form)

    if not os.path.exists(conversations_db_path):
        conversation = Conversation(conversations_db_path)
        conversation.initialise_table()

    return jsonify({
        "success": True
    })   

@app.route("/get_message_history", methods=["POST"]) 
def get_message_history():
    conversation_db_path = get_conversation_db_path_for_users(request.form)
    conversation = Conversation(conversation_db_path)
    
    history = conversation.get_history()
    return jsonify({
        "history": history
    })


if __name__ == '__main__':
    app.run(debug=True)