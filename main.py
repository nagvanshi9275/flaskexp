

from flask import Flask, request
from config import init_db
from models import User

app = Flask(__name__)

# Initialize the database
init_db(app)

# Route to add a user

@app.route('/')
def home():
    return "Welcome to the Flask app!"




@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json  # No parentheses needed, it's a property not a method
    
    # Creating a new user
    user = User(
        username=data['username'],  # Use colons (:) inside the constructor
        email=data['email'],
        age=data['age']
    )

    # Save the user to MongoDB
    user.save()

    # Return a success message
    return "User added successfully", 201  # Status 201 indicates successful creation

# Route to retrieve a user by username
@app.route('/get_user/<username>', methods=['GET'])  # 'GET' should be inside quotes
def get_user(username):
    # Retrieve the first user matching the username
    user = User.objects(username=username).first()

    if user:
        # Return user details if found
        return f"User found: {user.username}, Email: {user.email}, Age: {user.age}", 200
    else:
        # Return an error message if the user is not found
        return "User not found", 404

# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)











