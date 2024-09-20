"""import os
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='src')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/openheimer')
def open():
    query = request.args.get('query')

    if query:
        return f"kya hua {query}"  # Properly indented
    else:
        return "kuch likho na"  # Properly indented

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)

if __name__ == '__main__':
    main()

   from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Replace the URI string with your MongoDB Atlas connection string
mongo_uri = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client.get_database('myFirstDatabase')  # Replace with your database name

@app.route('/')
def home():
    # Example of inserting a document
    collection = db.myCollection  # Replace with your collection name
    collection.insert_one({"name": "Flask", "type": "framework"})
    return "Connected to MongoDB Atlas with Flask!"

if __name__ == '__main__':
    app.run(debug=True)






"""
"""import os
from flask import Flask 
from pymongo import MongoClient

app = Flask(__name__)

mongo_uri = "mongodb+srv://nagvanshi:nagvanshi123@cluster0.82qda.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(mongo_uri)

db = client.get_database('internship1')

collection = db['myCollection']

@app.route('/')
def home():
    return "Connected to MongasasoDB Atlas! Available Collections"

@app.route('/addeddata', methods=['POST'])
def adddata():
    data = {
        "Name": "Ashish Nagvanshi",
        "email": "aashishsingh24032005@gmail.com",
        "age": "20"
    }
    result = collection.insert_one(data)
    return f"Data inserted with ID: {result.inserted_id}"

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)

if __name__ == '__main__':
    main()

"""

import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

mongo_uri = "mongodb+srv://nagvanshi:nagvanshi123@cluster0.82qda.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)
db = client.get_database('internship1')
collection = db['myCollection']

@app.route('/')
def home():
    return "Connected to MongoDB Atlas! Available Collections"

@app.route('/addeddata', methods=['POST'])
def addata():
    data = {
        "Name": "King",
        "age": "21",
        "email": "king@123"
    }
    result = collection.insert_one(data)
    return f"Data is added successfully with id {result.inserted_id}"

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)

if __name__ == '__main__':
    main()






